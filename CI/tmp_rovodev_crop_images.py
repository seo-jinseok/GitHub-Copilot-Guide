#!/usr/bin/env python3
"""
PNG 파일에서 개별 이미지들을 자동으로 감지하고 크롭하여 별도 파일로 저장하는 스크립트
"""

import os
import numpy as np
from PIL import Image, ImageDraw
import glob

def find_bounding_boxes(image_array, threshold=240, min_area=1000):
    """
    이미지에서 개별 객체들의 바운딩 박스를 찾는 함수
    """
    # 그레이스케일로 변환
    if len(image_array.shape) == 3:
        gray = np.mean(image_array, axis=2)
    else:
        gray = image_array
    
    # 배경을 흰색(255)으로 가정하고, 임계값보다 어두운 픽셀을 찾음
    mask = gray < threshold
    
    # 연결된 컴포넌트 찾기 (간단한 flood fill 방식)
    visited = np.zeros_like(mask, dtype=bool)
    components = []
    
    def flood_fill(start_y, start_x):
        """간단한 flood fill 알고리즘"""
        stack = [(start_y, start_x)]
        component_pixels = []
        
        while stack:
            y, x = stack.pop()
            if (y < 0 or y >= mask.shape[0] or 
                x < 0 or x >= mask.shape[1] or 
                visited[y, x] or not mask[y, x]):
                continue
                
            visited[y, x] = True
            component_pixels.append((y, x))
            
            # 8방향 탐색
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    stack.append((y + dy, x + dx))
        
        return component_pixels
    
    # 모든 픽셀을 검사하여 연결된 컴포넌트 찾기
    for y in range(mask.shape[0]):
        for x in range(mask.shape[1]):
            if mask[y, x] and not visited[y, x]:
                component = flood_fill(y, x)
                if len(component) > min_area:  # 최소 크기 필터
                    components.append(component)
    
    # 각 컴포넌트의 바운딩 박스 계산
    bounding_boxes = []
    for component in components:
        if not component:
            continue
            
        ys, xs = zip(*component)
        min_y, max_y = min(ys), max(ys)
        min_x, max_x = min(xs), max(xs)
        
        # 패딩 추가
        padding = 10
        min_y = max(0, min_y - padding)
        min_x = max(0, min_x - padding)
        max_y = min(mask.shape[0] - 1, max_y + padding)
        max_x = min(mask.shape[1] - 1, max_x + padding)
        
        bounding_boxes.append((min_x, min_y, max_x, max_y))
    
    return bounding_boxes

def crop_and_save_images(input_file, output_dir):
    """
    입력 이미지에서 개별 객체들을 크롭하여 저장
    """
    print(f"\n처리 중: {input_file}")
    
    # 이미지 로드
    image = Image.open(input_file)
    image_array = np.array(image)
    
    print(f"이미지 크기: {image.size}")
    
    # 바운딩 박스 찾기
    bounding_boxes = find_bounding_boxes(image_array)
    
    print(f"발견된 객체 수: {len(bounding_boxes)}")
    
    if not bounding_boxes:
        print("객체를 찾을 수 없습니다. 임계값을 조정해보세요.")
        return
    
    # 출력 디렉토리 생성
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_subdir = os.path.join(output_dir, base_name)
    os.makedirs(output_subdir, exist_ok=True)
    
    # 각 바운딩 박스에 대해 크롭 및 저장
    for i, (x1, y1, x2, y2) in enumerate(bounding_boxes):
        # 크롭
        cropped = image.crop((x1, y1, x2, y2))
        
        # 파일명 생성
        output_filename = f"{base_name}_object_{i+1:02d}.png"
        output_path = os.path.join(output_subdir, output_filename)
        
        # 저장
        cropped.save(output_path)
        print(f"저장됨: {output_filename} (크기: {cropped.size})")
    
    # 바운딩 박스를 표시한 원본 이미지도 저장 (참고용)
    debug_image = image.copy()
    draw = ImageDraw.Draw(debug_image)
    
    for i, (x1, y1, x2, y2) in enumerate(bounding_boxes):
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
        draw.text((x1, y1-20), f"Object {i+1}", fill="red")
    
    debug_path = os.path.join(output_subdir, f"{base_name}_debug_boxes.png")
    debug_image.save(debug_path)
    print(f"디버그 이미지 저장됨: {debug_path}")

def main():
    """메인 함수"""
    print("=== PNG 이미지 자동 크롭 도구 ===")
    
    # PNG 파일들 찾기
    png_files = glob.glob("*.png")
    png_files = [f for f in png_files if not f.startswith("tmp_")]  # 임시 파일 제외
    
    if not png_files:
        print("PNG 파일을 찾을 수 없습니다.")
        return
    
    print(f"발견된 PNG 파일: {png_files}")
    
    # 출력 디렉토리 생성
    output_dir = "cropped_images"
    os.makedirs(output_dir, exist_ok=True)
    
    # 각 PNG 파일 처리
    for png_file in png_files:
        try:
            crop_and_save_images(png_file, output_dir)
        except Exception as e:
            print(f"오류 발생 ({png_file}): {e}")
    
    print(f"\n완료! 크롭된 이미지들이 '{output_dir}' 폴더에 저장되었습니다.")

if __name__ == "__main__":
    main()