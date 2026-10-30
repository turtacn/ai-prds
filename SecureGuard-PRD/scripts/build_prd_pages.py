import os

base_dir = "SecureGuard-PRD"

# Navigation mapping for header generation
nav_items = [
    ("index.html", "fa-home", "产品概览首页", "root"),
    ("01-executive-summary/summary.html", "fa-file-contract", "执行摘要", "01"),
    ("02-market-analysis/market-overview.html", "fa-chart-line", "市场概况", "02"),
    ("02-market-analysis/competitor-analysis.html", "fa-chess", "竞品分析", "02"),
    ("02-market-analysis/target-users.html", "fa-users", "目标用户画像", "02"),
    ("03-product-vision/vision-mission.html", "fa-bullseye", "愿景与使命", "03"),
    ("03-product-vision/core-problems.html", "fa-exclamation-triangle", "核心问题定义", "03"),
    ("03-product-vision/value-proposition.html", "fa-gem", "核心价值主张", "03"),
    ("04-functional-requirements/module-cve-scanning.html", "fa-bug", "CVE漏洞扫描模块", "04"),
    ("04-functional-requirements/module-gdpr-compliance.html", "fa-user-shield", "GDPR合规模块", "04"),
    ("04-functional-requirements/module-risk-prioritization.html", "fa-sort-amount-up-alt", "风险优先级引擎", "04"),
    ("04-functional-requirements/module-remediation.html", "fa-wrench", "修复闭环管理", "04"),
    ("04-functional-requirements/module-audit-reporting.html", "fa-file-invoice", "审计报告生成", "04"),
    ("05-technical-architecture/system-architecture.html", "fa-sitemap", "系统架构图", "05"),
    ("05-technical-architecture/data-flow.html", "fa-project-diagram", "数据流设计", "05"),
    ("05-technical-architecture/integration-apis.html", "fa-network-wired", "集成接口 API", "05"),
    ("06-user-experience/user-journey.html", "fa-route", "用户旅程地图", "06"),
    ("06-user-experience/dashboard-mockup.html", "fa-desktop", "控制台界面原型", "06"),
    ("06-user-experience/workflow-scenarios.html", "fa-tasks", "典型工作流场景", "06"),
    ("07-implementation-roadmap/phase1-mvp.html", "fa-rocket", "Phase 1: MVP", "07"),
    ("07-implementation-roadmap/phase2-expansion.html", "fa-expand-arrows-alt", "Phase 2: 功能扩展", "07"),
    ("07-implementation-roadmap/phase3-ai-automation.html", "fa-robot", "Phase 3: AI自动化", "07"),
    ("08-compliance-framework/gdpr-mapping.html", "fa-scale-balanced", "GDPR条款映射", "08"),
    ("08-compliance-framework/iso27001-alignment.html", "fa-certificate", "ISO 27001对齐", "08"),
    ("08-compliance-framework/cisa-kev-integration.html", "fa-shield-cat", "CISA KEV集成", "08"),
    ("09-pricing-licensing/pricing-model.html", "fa-tags", "定价与授权模式", "09"),
    ("10-appendix/glossary.html", "fa-book", "术语表", "10"),
    ("10-appendix/references.html", "fa-link", "参考资料与来源", "10"),
]

def render_sidebar(current_rel_path, rel_prefix):
    sidebar_html = f'''
        <nav class="sidebar">
            <div class="sidebar-header">
                <div class="brand-logo">
                    <i class="fas fa-shield-halved"></i>
                    <div>
                        <span>SecureGuard</span>
                        <div class="brand-tagline">SGCS PRD v1.0</div>
                    </div>
                </div>
            </div>
            <div class="sidebar-nav">
                <a href="{rel_prefix}index.html" class="nav-item {"active" if current_rel_path == "index.html" else ""}">
                    <i class="fas fa-home"></i> 产品概览首页
                </a>

                <div class="nav-section">
                    <div class="nav-section-title">01 执行摘要</div>
                    <a href="{rel_prefix}01-executive-summary/summary.html" class="nav-item {"active" if "summary.html" in current_rel_path else ""}">
                        <i class="fas fa-file-contract"></i> 执行摘要
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">02 市场分析</div>
                    <a href="{rel_prefix}02-market-analysis/market-overview.html" class="nav-item {"active" if "market-overview" in current_rel_path else ""}">
                        <i class="fas fa-chart-line"></i> 市场概况
                    </a>
                    <a href="{rel_prefix}02-market-analysis/competitor-analysis.html" class="nav-item {"active" if "competitor-analysis" in current_rel_path else ""}">
                        <i class="fas fa-chess"></i> 竞品分析
                    </a>
                    <a href="{rel_prefix}02-market-analysis/target-users.html" class="nav-item {"active" if "target-users" in current_rel_path else ""}">
                        <i class="fas fa-users"></i> 目标用户画像
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">03 产品愿景与定位</div>
                    <a href="{rel_prefix}03-product-vision/vision-mission.html" class="nav-item {"active" if "vision-mission" in current_rel_path else ""}">
                        <i class="fas fa-bullseye"></i> 愿景与使命
                    </a>
                    <a href="{rel_prefix}03-product-vision/core-problems.html" class="nav-item {"active" if "core-problems" in current_rel_path else ""}">
                        <i class="fas fa-exclamation-triangle"></i> 核心问题定义
                    </a>
                    <a href="{rel_prefix}03-product-vision/value-proposition.html" class="nav-item {"active" if "value-proposition" in current_rel_path else ""}">
                        <i class="fas fa-gem"></i> 核心价值主张
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">04 功能需求</div>
                    <a href="{rel_prefix}04-functional-requirements/module-cve-scanning.html" class="nav-item {"active" if "module-cve-scanning" in current_rel_path else ""}">
                        <i class="fas fa-bug"></i> CVE漏洞扫描模块
                    </a>
                    <a href="{rel_prefix}04-functional-requirements/module-gdpr-compliance.html" class="nav-item {"active" if "module-gdpr-compliance" in current_rel_path else ""}">
                        <i class="fas fa-user-shield"></i> GDPR合规模块
                    </a>
                    <a href="{rel_prefix}04-functional-requirements/module-risk-prioritization.html" class="nav-item {"active" if "module-risk-prioritization" in current_rel_path else ""}">
                        <i class="fas fa-sort-amount-up-alt"></i> 风险优先级引擎
                    </a>
                    <a href="{rel_prefix}04-functional-requirements/module-remediation.html" class="nav-item {"active" if "module-remediation" in current_rel_path else ""}">
                        <i class="fas fa-wrench"></i> 修复闭环管理
                    </a>
                    <a href="{rel_prefix}04-functional-requirements/module-audit-reporting.html" class="nav-item {"active" if "module-audit-reporting" in current_rel_path else ""}">
                        <i class="fas fa-file-invoice"></i> 审计报告生成
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">05 技术架构</div>
                    <a href="{rel_prefix}05-technical-architecture/system-architecture.html" class="nav-item {"active" if "system-architecture" in current_rel_path else ""}">
                        <i class="fas fa-sitemap"></i> 系统架构图
                    </a>
                    <a href="{rel_prefix}05-technical-architecture/data-flow.html" class="nav-item {"active" if "data-flow" in current_rel_path else ""}">
                        <i class="fas fa-project-diagram"></i> 数据流设计
                    </a>
                    <a href="{rel_prefix}05-technical-architecture/integration-apis.html" class="nav-item {"active" if "integration-apis" in current_rel_path else ""}">
                        <i class="fas fa-network-wired"></i> 集成接口 API
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">06 用户体验</div>
                    <a href="{rel_prefix}06-user-experience/user-journey.html" class="nav-item {"active" if "user-journey" in current_rel_path else ""}">
                        <i class="fas fa-route"></i> 用户旅程地图
                    </a>
                    <a href="{rel_prefix}06-user-experience/dashboard-mockup.html" class="nav-item {"active" if "dashboard-mockup" in current_rel_path else ""}">
                        <i class="fas fa-desktop"></i> 控制台界面原型
                    </a>
                    <a href="{rel_prefix}06-user-experience/workflow-scenarios.html" class="nav-item {"active" if "workflow-scenarios" in current_rel_path else ""}">
                        <i class="fas fa-tasks"></i> 典型工作流场景
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">07 实施路线图</div>
                    <a href="{rel_prefix}07-implementation-roadmap/phase1-mvp.html" class="nav-item {"active" if "phase1-mvp" in current_rel_path else ""}">
                        <i class="fas fa-rocket"></i> Phase 1: MVP
                    </a>
                    <a href="{rel_prefix}07-implementation-roadmap/phase2-expansion.html" class="nav-item {"active" if "phase2-expansion" in current_rel_path else ""}">
                        <i class="fas fa-expand-arrows-alt"></i> Phase 2: 功能扩展
                    </a>
                    <a href="{rel_prefix}07-implementation-roadmap/phase3-ai-automation.html" class="nav-item {"active" if "phase3-ai-automation" in current_rel_path else ""}">
                        <i class="fas fa-robot"></i> Phase 3: AI自动化
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">08 合规框架映射</div>
                    <a href="{rel_prefix}08-compliance-framework/gdpr-mapping.html" class="nav-item {"active" if "gdpr-mapping" in current_rel_path else ""}">
                        <i class="fas fa-scale-balanced"></i> GDPR条款映射
                    </a>
                    <a href="{rel_prefix}08-compliance-framework/iso27001-alignment.html" class="nav-item {"active" if "iso27001-alignment" in current_rel_path else ""}">
                        <i class="fas fa-certificate"></i> ISO 27001对齐
                    </a>
                    <a href="{rel_prefix}08-compliance-framework/cisa-kev-integration.html" class="nav-item {"active" if "cisa-kev-integration" in current_rel_path else ""}">
                        <i class="fas fa-shield-cat"></i> CISA KEV集成
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">09 商业与定价</div>
                    <a href="{rel_prefix}09-pricing-licensing/pricing-model.html" class="nav-item {"active" if "pricing-model" in current_rel_path else ""}">
                        <i class="fas fa-tags"></i> 定价与授权模式
                    </a>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">10 附录</div>
                    <a href="{rel_prefix}10-appendix/glossary.html" class="nav-item {"active" if "glossary" in current_rel_path else ""}">
                        <i class="fas fa-book"></i> 术语表
                    </a>
                    <a href="{rel_prefix}10-appendix/references.html" class="nav-item {"active" if "references" in current_rel_path else ""}">
                        <i class="fas fa-link"></i> 参考资料与来源
                    </a>
                </div>
            </div>
            <div class="sidebar-footer">
                <span><i class="fas fa-lock"></i> SGCS Internal</span>
                <span>v1.0 Final</span>
            </div>
        </nav>
    '''
    return sidebar_html

def page_wrapper(title, section_name, current_rel_path, content_body):
    rel_prefix = "../" if "/" in current_rel_path else ""
    sidebar = render_sidebar(current_rel_path, rel_prefix)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - SecureGuard PRD</title>
    <link rel="stylesheet" href="{rel_prefix}assets/css/main.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({{startOnLoad:true, theme: 'neutral'}});</script>
</head>
<body>
    <div class="app-container">
        {sidebar}
        <div class="main-wrapper">
            <header class="top-navbar">
                <div class="top-navbar-left">
                    <button class="toggle-sidebar-btn" id="toggleSidebarBtn"><i class="fas fa-bars"></i></button>
                    <div class="search-box">
                        <i class="fas fa-search"></i>
                        <input type="text" id="globalSearchInput" placeholder="搜索 PRD 文档、功能、API...">
                    </div>
                </div>
                <div class="top-navbar-right">
                    <span class="version-badge">v1.0 PRD</span>
                    <button class="theme-toggle-btn" id="themeToggleBtn"><i class="fas fa-moon"></i> 深色模式</button>
                </div>
            </header>

            <main class="content-area">
                <div class="breadcrumb">
                    <a href="{rel_prefix}index.html">SGCS PRD</a> <i class="fas fa-chevron-right"></i>
                    <span>{section_name}</span> <i class="fas fa-chevron-right"></i>
                    <span class="breadcrumb-current">{title}</span>
                </div>

                {content_body}

                <footer class="prd-footer">
                    <div>© 2024 SecureGuard Product Team. Confidential - For Internal PRD Review Only.</div>
                    <div>文档状态: <span class="badge badge-success">Approved v1.0</span></div>
                </footer>
            </main>
        </div>
    </div>
    <script src="{rel_prefix}assets/js/main.js"></script>
</body>
</html>'''
    return html

print("Generator helper defined successfully.")
