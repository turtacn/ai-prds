import os
from playwright.sync_api import sync_playwright

diagrams = {
    "trend_chart.png": '''
        xychart-beta
            title "近 30 天 CVE 漏洞与 GDPR DSAR 工单收敛趋势"
            x-axis ["Week 1", "Week 2", "Week 3", "Week 4"]
            y-axis "工单数量 (件)" 0 --> 200
            line [150, 120, 85, 38]
            line [24, 18, 12, 5]
    ''',
    "system_architecture.png": '''
        graph TD
            subgraph Client_Layer ["客户端与接入层"]
                UI["Web 控制台 / UI"]
                API_GW["API 网关 / Kong Gateway"]
            end

            subgraph SGCS_Engine ["SGCS 核心微服务引擎 (Kubernetes Cluster)"]
                Scanner["CVE 扫描微服务 Engine"]
                PII_Finder["PII 数据识别 Engine"]
                Risk_Engine["智能风险关联引擎 (PRE Engine)"]
                Rem_Engine["修复与虚拟补丁 Engine"]
                Audit_Engine["审计与证据链 Engine"]
            end

            subgraph Storage_Layer ["数据持久化与存储层"]
                DB[("PostgreSQL - 业务与配置")]
                ES[("ElasticSearch - 漏洞与日志库")]
                Redis[("Redis - 高速缓存 & 队列")]
            end

            subgraph External_Layer ["外部数据源与集成"]
                NVD["NVD / CISA KEV / EPSS"]
                Integrations["Jira / ServiceNow / Splunk SIEM"]
            end

            UI --> API_GW
            API_GW --> Scanner
            API_GW --> PII_Finder
            API_GW --> Risk_Engine
            Scanner --> ES
            PII_Finder --> ES
            Risk_Engine --> DB
            Rem_Engine --> Integrations
            NVD --> Scanner
    ''',
    "data_flow.png": '''
        sequenceDiagram
            autonumber
            participant Asset as 客户主机/云资产
            participant Agent as SGCS Agent/Scanner
            participant Engine as 智能风险关联引擎
            participant Ticket as Jira/ServiceNow
            participant Audit as 合规证据库

            Asset->>Agent: 1. 上报 OS/组件清单与 PII 特征
            Agent->>Engine: 2. 传输资产漏洞与数据敏感度元数据
            Engine->>Engine: 3. 匹配 CISA KEV + 计算 PRE 风险暴露值
            Engine->>Ticket: 4. 超过 SLA 阈值自动触发工单指派
            Engine->>Audit: 5. 生成不可篡改的合规审计日志与时间戳
    ''',
    "roadmap_gantt.png": '''
        gantt
            title SGCS 产品路线图 (Roadmap 2024)
            dateFormat YYYY-MM-DD
            section Q1: MVP
            核心 CVE 扫描与基础 PII :active, p1, 2024-01-01, 2024-03-31
            section Q2-Q3: Expansion
            虚拟补丁与 Jira/ServiceNow 集成 :p2, 2024-04-01, 2024-09-30
            section Q4: AI & Global
            AI 风险预测与全球数据中心部署 :p3, 2024-10-01, 2024-12-31
    '''
}

def convert_mermaid_to_png():
    output_dir = "SecureGuard-PRD/assets/images"
    os.makedirs(output_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1000, "height": 800})

        for filename, code in diagrams.items():
            html_doc = f'''<!DOCTYPE html>
            <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
                <script>mermaid.initialize({{startOnLoad:true, theme: 'neutral'}});</script>
                <style>
                    body {{ background: #ffffff; margin: 0; padding: 20px; display: inline-block; }}
                    .mermaid {{ font-family: sans-serif; }}
                </style>
            </head>
            <body>
                <div class="mermaid">{code}</div>
            </body>
            </html>'''

            page.set_content(html_doc)
            page.wait_for_selector('.mermaid svg', timeout=10000)
            element = page.query_selector('body')
            file_path = os.path.join(output_dir, filename)
            element.screenshot(path=file_path)
            print(f"Generated {file_path}")

        browser.close()

if __name__ == "__main__":
    convert_mermaid_to_png()
