---
layout: default
lang: en
---

<style>
  /* Landing Page Specific Styles */
  .hero-section {
    background: linear-gradient(135deg, #003DA5 0%, #0051D5 50%, #0066FF 100%);
    color: white;
    padding: 80px 20px;
    margin: -20px -20px 40px -20px;
    text-align: center;
    border-radius: 0 0 20px 20px;
    box-shadow: 0 8px 24px rgba(0, 61, 165, 0.2);
  }

  .hero-logo {
    width: 120px;
    height: 120px;
    margin: 0 auto 30px;
    background: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    padding: 20px;
  }

  .hero-logo img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    border: none !important;
    box-shadow: none !important;
    margin: 0 !important;
  }

  .hero-title {
    font-size: 42px;
    font-weight: 800;
    margin: 0 0 15px 0;
    letter-spacing: -1px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  }

  .hero-subtitle {
    font-size: 20px;
    font-weight: 400;
    margin: 0 0 30px 0;
    opacity: 0.95;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.6;
  }

  .hero-badges {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 20px;
  }

  .hero-badge {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 14px;
    font-weight: 600;
    border: 2px solid rgba(255, 255, 255, 0.3);
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    margin: 50px 0;
  }

  .feature-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 2px solid #e1e4e8;
    border-radius: 16px;
    padding: 30px;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  }

  .feature-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 28px rgba(0, 61, 165, 0.15);
    border-color: #003DA5;
  }

  .feature-icon {
    font-size: 48px;
    margin-bottom: 20px;
    display: block;
  }

  .feature-title {
    font-size: 20px;
    font-weight: 700;
    color: #003DA5;
    margin: 0 0 15px 0;
  }

  .feature-description {
    font-size: 15px;
    color: #586069;
    line-height: 1.6;
    margin: 0 0 20px 0;
  }

  .feature-cta {
    display: inline-block;
    background: linear-gradient(135deg, #003DA5 0%, #0051D5 100%);
    color: white;
    text-decoration: none;
    padding: 12px 28px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 61, 165, 0.2);
  }

  .feature-cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 61, 165, 0.3);
    background: linear-gradient(135deg, #002D7D 0%, #003DA5 100%);
  }

  .roles-section {
    margin: 60px 0;
  }

  .roles-title {
    text-align: center;
    font-size: 32px;
    font-weight: 800;
    color: #003DA5;
    margin: 0 0 15px 0;
  }

  .roles-subtitle {
    text-align: center;
    font-size: 16px;
    color: #586069;
    margin: 0 0 40px 0;
  }

  .roles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
  }

  .role-card {
    background: white;
    border: 2px solid #e1e4e8;
    border-radius: 12px;
    padding: 25px;
    text-align: center;
    transition: all 0.3s ease;
  }

  .role-card:hover {
    border-color: #003DA5;
    box-shadow: 0 8px 20px rgba(0, 61, 165, 0.12);
  }

  .role-icon {
    font-size: 40px;
    margin-bottom: 15px;
    display: block;
  }

  .role-title {
    font-size: 18px;
    font-weight: 700;
    color: #24292e;
    margin: 0 0 15px 0;
  }

  .role-links {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .role-link {
    display: inline-block;
    color: #003DA5;
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
    padding: 8px 16px;
    border-radius: 6px;
    transition: all 0.2s ease;
  }

  .role-link:hover {
    background: #f0f4ff;
  }

  .role-link.disabled {
    color: #999;
    cursor: not-allowed;
  }

  .role-link.disabled:hover {
    background: transparent;
  }

  .cta-section {
    background: linear-gradient(135deg, #f6f8fa 0%, #e1e4e8 100%);
    border-radius: 16px;
    padding: 50px 30px;
    text-align: center;
    margin: 60px 0;
  }

  .cta-title {
    font-size: 28px;
    font-weight: 700;
    color: #24292e;
    margin: 0 0 15px 0;
  }

  .cta-description {
    font-size: 16px;
    color: #586069;
    margin: 0 0 30px 0;
  }

  .cta-button {
    display: inline-block;
    background: linear-gradient(135deg, #28a745 0%, #22863a 100%);
    color: white;
    text-decoration: none;
    padding: 16px 40px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 6px 16px rgba(40, 167, 69, 0.3);
  }

  .cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(40, 167, 69, 0.4);
  }

  @media (max-width: 768px) {
    .hero-title {
      font-size: 32px;
    }
    
    .hero-subtitle {
      font-size: 16px;
    }

    .features-grid {
      grid-template-columns: 1fr;
    }

    .roles-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<!-- Hero Section -->
<div class="hero-section">
  <div class="hero-logo">
    <img src="../images/ci/deu.svg" alt="Dong-Eui University Logo" onerror="this.style.display='none'">
  </div>
  <h1 class="hero-title">Mastering GitHub Copilot</h1>
  <p class="hero-subtitle">
    AI Coding Assistant Guide for Dong-Eui University Members<br>
    Learn everything from installation to expert usage
  </p>
  <div class="hero-badges">
    <span class="hero-badge">✅ Start for Free</span>
    <span class="hero-badge">🚀 Fast Learning</span>
    <span class="hero-badge">💼 Practical Application</span>
  </div>
</div>

<!-- Features Section -->
<div class="features-grid">
  <div class="feature-card">
    <span class="feature-icon">🌐</span>
    <h2 class="feature-title">Start on the Web</h2>
    <p class="feature-description">
      Experience GitHub Copilot for free in your web browser without complex installation
    </p>
    <a href="../common/en/copilot_web.html" class="feature-cta">Start Now →</a>
  </div>

  <div class="feature-card">
    <span class="feature-icon">💻</span>
    <h2 class="feature-title">Pro with VS Code</h2>
    <p class="feature-description">
      Install VS Code and learn professional usage tailored to your role
    </p>
    <a href="#roles" class="feature-cta">View Role Guides →</a>
  </div>

  <div class="feature-card">
    <span class="feature-icon">📚</span>
    <h2 class="feature-title">Step-by-Step Learning</h2>
    <p class="feature-description">
      Improve your skills with a systematic curriculum from beginner to expert
    </p>
    <a href="../common/en/copilot_web.html" class="feature-cta">Start Learning →</a>
  </div>
</div>

<!-- Roles Section -->
<div class="roles-section" id="roles">
  <h2 class="roles-title">Customized Guides by Role</h2>
  <p class="roles-subtitle">Choose the guide that fits your role</p>
  
  <div class="roles-grid">
    <div class="role-card">
      <span class="role-icon">👔</span>
      <h3 class="role-title">Admin Staff</h3>
      <div class="role-links">
        <a href="../admin/ko/" class="role-link">🇰🇷 Korean Guide</a>
        <a href="../admin/en/" class="role-link">🇺🇸 English Guide</a>
      </div>
    </div>

    <div class="role-card">
      <span class="role-icon">👨‍🏫</span>
      <h3 class="role-title">Professor</h3>
      <div class="role-links">
        <a href="../professor/ko/" class="role-link">🇰🇷 Korean Guide</a>
        <span class="role-link disabled">🇺🇸 Coming Soon</span>
      </div>
    </div>

    <div class="role-card">
      <span class="role-icon">🎓</span>
      <h3 class="role-title">Student</h3>
      <div class="role-links">
        <a href="../student/ko/" class="role-link">🇰🇷 Korean Guide</a>
        <span class="role-link disabled">🇺🇸 Coming Soon</span>
      </div>
    </div>

    <div class="role-card">
      <span class="role-icon">🧪</span>
      <h3 class="role-title">Researcher</h3>
      <div class="role-links">
        <a href="../researcher/ko/" class="role-link">🇰🇷 Korean Guide</a>
        <span class="role-link disabled">🇺🇸 Coming Soon</span>
      </div>
    </div>
  </div>
</div>

<!-- CTA Section -->
<div class="cta-section">
  <h2 class="cta-title">Start Right Now!</h2>
  <p class="cta-description">
    Experience GitHub Copilot in 5 minutes with the web version, no installation required
  </p>
  <a href="../common/en/copilot_web.html" class="cta-button">Start for Free 🚀</a>
</div>
