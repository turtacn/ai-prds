import os
from build_prd_pages import page_wrapper, base_dir

pages_data = {}

# Section 04: Functional Requirements
pages_data["04-functional-requirements/module-cve-scanning.html"] = ("CVE漏洞扫描模块", "04 功能需求", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-bug"></i> CVE漏洞扫描模块 (CVE Scanning Engine)</h1>
    <p class="page-subtitle">全面覆盖操作系统、容器、云工作负载与开源组件的全栈漏洞检测功能</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-list-check"></i> 核心功能规格说明</h3></div>
    <div class="table-responsive">
        <table class="data-table">
            <thead>
                <tr>
                    <th>功能编号</th>
                    <th>功能特性</th>
                    <th>说明与技术实现</th>
                    <th>优先级</th>
                    <th>成功指标 (KPI)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>CVE-01</td>
                    <td>双模扫描机制</td>
                    <td>支持轻量级 Agent 实时监控与 Agentless 协议扫描（SSH/WMI/Cloud API），适应混合云架构。</td>
                    <td><span class="badge badge-critical">P0</span></td>
                    <td>覆盖率 99.9% 资产，无盲区检测</td>
                </tr>
                <tr>
                    <td>CVE-02</td>
                    <td>实时漏洞特征库同步</td>
                    <td>对接 NVD/CVE、CISA KEV、GitHub Advisory 及厂商漏洞源，实现每 15 分钟增量更新。</td>
                    <td><span class="badge badge-critical">P0</span></td>
                    <td>漏洞特征库更新延迟 < 15 分钟</td>
                </tr>
                <tr>
                    <td>CVE-03</td>
                    <td>开源组件 SCA 扫描</td>
                    <td>深度解析 Maven, npm, PyPI, Go, Cargo 等依赖项，识别已知开源漏洞（SCA）。</td>
                    <td><span class="badge badge-high">P1</span></td>
                    <td>误报率 < 2%，准确识别嵌套依赖</td>
                </tr>
                <tr>
                    <td>CVE-04</td>
                    <td>CISA KEV 优先高亮</td>
                    <td>自动匹配 CISA Known Exploited Vulnerabilities 目录，优先标记已被实际利用的漏洞。</td>
                    <td><span class="badge badge-critical">P0</span></td>
                    <td>100% 自动对齐 CISA KEV 库</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="callout warning">
    <div class="callout-title"><i class="fas fa-exclamation-circle"></i> 性能与安全标准</div>
    <p> Agentless 扫描在单台服务器上的 CPU 占用率不得超过 5%，内存占用 < 128MB；扫描过程中不得对生产业务造成服务中断或网络拥堵。</p>
</div>
''')

pages_data["04-functional-requirements/module-gdpr-compliance.html"] = ("GDPR合规模块", "04 功能需求", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-user-shield"></i> GDPR合规模块 (GDPR Compliance Engine)</h1>
    <p class="page-subtitle">自动化 PII 敏感数据识别、DSAR 流程管理与 DPIA 评估</p>
</div>

<div class="grid-2">
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-search-location"></i> 自动化 PII 资产发现与映射</h3></div>
        <p>基于 NLP 与正则特征库，自动扫描结构化数据库（MySQL/PostgreSQL/MongoDB）与非结构化文件存储（S3/NFS），精准标记包含姓名、Email、身份证件、地理位置、信用卡等 30+ 种 GDPR 个人敏感数据 (PII)。</p>
    </div>
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-tasks"></i> 数据主体权利请求 (DSAR) 管理</h3></div>
        <p>内置标准 DSAR 响应门户，支持自动化查询、导出、访问及“被遗忘权（Right to be forgotten）”删除请求流水线。系统全流程记录日志，自动合规归档。</p>
    </div>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-file-signature"></i> DPIA 评估模板与 72小时违规响应</h3></div>
    <p>提供内置 DPIA（数据保护影响评估）自动化问卷与风险打分系统。当系统检测到含有 PII 的资产发生 Critical 级漏洞或安全事件时，自动触发 72 小时数据泄露通知预警与执法报告生成器。</p>
</div>
''')

pages_data["04-functional-requirements/module-risk-prioritization.html"] = ("风险优先级引擎", "04 功能需求", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-sort-amount-up-alt"></i> 智能风险优先级引擎 (Risk Prioritization Engine)</h1>
    <p class="page-subtitle">业内首创：CVE 漏洞严重度与 GDPR PII 敏感资产价值深度融合计算</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-calculator"></i> 隐私风险暴露值 (PRE) 计算公式</h3></div>
    <div class="code-block">
        <code>
Privacy Risk Exposure (PRE) = [CVSS_v3/v4 Score × EPSS Exploitation Probability]
                              × [PII Asset Sensitivity Weight (1-5)]
                              × [CISA KEV Multiplier (1.5x)]
                              × [Network Exposure Index (Internal vs Internet)]
        </code>
    </div>
    <p style="font-size: 0.9rem; color: var(--text-secondary);">通过该公式，系统能够将原本分散的 10,000+ 漏洞收敛为最关键的前 20 个需立即修复的高隐患项，大幅释放 SecOps 团队人力。</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-layer-group"></i> 风险评级分类标准</h3></div>
    <div class="table-responsive">
        <table class="data-table">
            <thead>
                <tr><th>风险级别</th><th>PRE 分数区间</th><th>典型场景示例</th><th>响应 SLA 标准</th></tr>
            </thead>
            <tbody>
                <tr><td><span class="badge badge-critical">Critical</span></td><td>PRE >= 85</td><td>公网暴露的 Web 服务存在 RCE 漏洞，且后端连接存储 10万+ 客户信用卡数据的 DB</td><td>24 小时内修复/补丁</td></tr>
                <tr><td><span class="badge badge-high">High</span></td><td>65 <= PRE < 85</td><td>内网服务器存在 CISA KEV 漏洞，关联员工 PII 档案库</td><td>72 小时内修复</td></tr>
                <tr><td><span class="badge badge-medium">Medium</span></td><td>35 <= PRE < 65</td><td>开发环境存在高 CVSS 漏洞，但无真实 PII 数据关联</td><td>14 天内修复</td></tr>
            </tbody>
        </table>
    </div>
</div>
''')

pages_data["04-functional-requirements/module-remediation.html"] = ("修复闭环管理", "04 功能需求", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-wrench"></i> 修复闭环管理 (Remediation Workflow)</h1>
    <p class="page-subtitle">从漏洞发现、工单指派、虚拟补丁应用到二次验证的标准化闭环</p>
</div>

<div class="grid-2">
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-shield-cat"></i> 无补丁虚拟防护 (Patchless Protection)</h3></div>
        <p>针对需要高可用保障、无法立即停机重启打补丁的生产服务器，SGCS 风险引擎自动生成匹配的 WAF 防护规则（如 ModSecurity, AWS WAF）或 eBPF 级别的进程拦截指令，即刻阻断漏洞利用。</p>
    </div>
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-sync-alt"></i> 自动工单指派与二次校验</h3></div>
        <p>双向集成 Jira、ServiceNow 和 GitHub Issues。自动指派责任人并追踪修复状态。补丁部署完成后，系统触发自动二次扫描，校验漏洞是否真正消除，消除后自动关闭工单。</p>
    </div>
</div>
''')

pages_data["04-functional-requirements/module-audit-reporting.html"] = ("审计报告生成", "04 功能需求", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-file-invoice"></i> 审计报告生成 (Audit & Reporting Engine)</h1>
    <p class="page-subtitle">面向 CISO、DPO 与外部监管机构（DPA）的合规证据链报告</p>
</div>

<div class="grid-3">
    <div class="card">
        <h3>1. CISO 管理层看板报告</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">高管视角的安全风险趋势、SLA 达成率、资产健康度与投资回报率 (ROI) 图表。</p>
    </div>
    <div class="card">
        <h3>2. GDPR DPA 合规证据包</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">符合欧盟监管标准的合规证据导出包，包含漏洞扫描记录、补丁日志、时间戳与数字签名。</p>
    </div>
    <div class="card">
        <h3>3. 技术工程师修复清单</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">细化到命令行级别的补丁安装步骤、配置修复指导与依赖关系图谱。</p>
    </div>
</div>
''')

# Section 05: Technical Architecture
pages_data["05-technical-architecture/system-architecture.html"] = ("系统架构图", "05 技术架构", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-sitemap"></i> 系统架构图 (System Architecture)</h1>
    <p class="page-subtitle">云原生、微服务化与混合多云部署架构</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-project-diagram"></i> SGCS 整体系统技术架构拓扑</h3></div>
    <div class="mermaid">
    graph TD
        subgraph 客户端与接入层
            UI[Web 控制台 / UI]
            API_GW[API 网关 / Kong Gateway]
        end

        subgraph SGCS 核心微服务引擎 (Kubernetes Cluster)
            Scanner[CVE 扫描微服务 Engine]
            PII_Finder[PII 数据识别 Engine]
            Risk_Engine[智能风险关联引擎 (PRE Engine)]
            Rem_Engine[修复与虚拟补丁 Engine]
            Audit_Engine[审计与证据链 Engine]
        end

        subgraph 数据持久化与存储层
            DB[(PostgreSQL - 业务与配置)]
            ES[(ElasticSearch - 漏洞与日志库)]
            Redis[(Redis - 高速缓存 & 队列)]
        end

        subgraph 外部数据源与集成
            NVD[NVD / CISA KEV / EPSS]
            Integrations[Jira / ServiceNow / Splunk SIEM]
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
    </div>
</div>
''')

pages_data["05-technical-architecture/data-flow.html"] = ("数据流设计", "05 技术架构", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-project-diagram"></i> 数据流设计 (Data Flow Architecture)</h1>
    <p class="page-subtitle">从资产采集、漏洞解析、风险计算到证据包落盘的数据流转过程</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-stream"></i> 端到端数据处理流水线</h3></div>
    <div class="mermaid">
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
    </div>
</div>
''')

pages_data["05-technical-architecture/integration-apis.html"] = ("集成接口 API", "05 技术架构", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-network-wired"></i> 集成接口 (RESTful APIs & Webhooks)</h1>
    <p class="page-subtitle">与企业现有生态系统（Jira, ServiceNow, Splunk）的开放集成方案</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-code"></i> API 示例：触发智能风险评估与工单生成</h3></div>
    <p><code>POST /api/v1/risk/evaluate-and-remediate</code></p>
    <div class="code-block">
        <code>
{
  "asset_id": "ast-89234710",
  "cve_id": "CVE-2023-38606",
  "pii_data_types": ["CREDIT_CARD", "PASSPORT"],
  "cvss_score": 9.8,
  "cisa_kev": true,
  "auto_remediate": true,
  "integration_target": "JIRA"
}
        </code>
    </div>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-plug"></i> 集成矩阵</h3></div>
    <ul>
        <li><strong>工单管理系统：</strong> Jira Cloud / On-Prem, ServiceNow ITSM, PagerDuty</li>
        <li><strong>SIEM / SOC 日志平台：</strong> Splunk Enterprise, Elastic SIEM, IBM QRadar</li>
        <li><strong>CI/CD 管道：</strong> GitLab CI, GitHub Actions, Jenkins</li>
    </ul>
</div>
''')

print("Section 04-05 generated in dictionary.")
