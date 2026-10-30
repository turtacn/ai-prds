import os
from build_prd_pages import page_wrapper, base_dir

pages_data = {}

# Section 01: Summary
pages_data["01-executive-summary/summary.html"] = ("执行摘要", "01 执行摘要", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-file-contract"></i> 执行摘要 (Executive Summary)</h1>
    <p class="page-subtitle">SGCS 平台战略定位、核心目标与商业前景概述</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-bullseye"></i> 项目背景与痛点</h3></div>
    <p>随着全球数据隐私法规（特别是欧盟 GDPR）的全面实施与罚金飙升，中大型企业面临着前所未有的双重安全合规挑战：一方面是日益严峻的 CVE 漏洞与网络威胁，另一方面是数据保护官（DPO）与 CISO 之间的技术与合规割裂。传统的漏洞扫描工具（如 Tenable、Qualys）仅关注技术风险，而合规管理平台（如 OneTrust）仅关注法律条款，缺少将漏洞风险与个人敏感数据（PII）资产实时关联的技术方案。</p>
</div>

<div class="grid-2">
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-shield-alt"></i> 产品核心定位</h3></div>
        <p><strong>SecureGuard Compliance Suite (SGCS)</strong> 是业内首个融合<strong>CVE 漏洞管理</strong>与<strong>GDPR 合规自动化</strong>的企业级统一安全平台。通过智能风险关联引擎，自动计算漏洞对 PII 数据资产的暴露风险，实现“扫描-排序-虚拟补丁/修复-合规举证”全闭环。</p>
    </div>
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-chart-line"></i> 商业价值与成功指标 (KPI)</h3></div>
        <ul>
            <li><strong>降低合规违规风险</strong>：减少 90% 以上涉及 PII 资产的 Critical/High 漏洞曝露时间。</li>
            <li><strong>提升响应效率</strong>：GDPR DSAR（数据主体请求）响应时间由 15 天缩短至 24 小时以内。</li>
            <li><strong>成功指标 (KPIs)</strong>：
                <ul>
                    <li>100% 满足 GDPR 72小时漏洞事件通知要求；</li>
                    <li>自动化生成审计可信证据包时间 < 5 分钟；</li>
                    <li>客户 TCO (总拥有成本) 较分别采购 Tenable+OneTrust 降低 40%。</li>
                </ul>
            </li>
        </ul>
    </div>
</div>
''')

# Section 02: Market Analysis
pages_data["02-market-analysis/market-overview.html"] = ("市场概况", "02 市场分析", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-chart-line"></i> 市场概况 (Market Overview)</h1>
    <p class="page-subtitle">全球网络安全与数据合规软件市场规模与演进趋势</p>
</div>

<div class="grid-3">
    <div class="stat-card">
        <div class="stat-icon primary"><i class="fas fa-dollar-sign"></i></div>
        <div><div class="stat-value">$24.5B</div><div class="stat-label">2024年全球漏洞管理与隐私合规市场</div></div>
    </div>
    <div class="stat-card">
        <div class="stat-icon success"><i class="fas fa-chart-line"></i></div>
        <div><div class="stat-value">18.4%</div><div class="stat-label">年复合增长率 (CAGR 2024-2028)</div></div>
    </div>
    <div class="stat-card">
        <div class="stat-icon high"><i class="fas fa-gavel"></i></div>
        <div><div class="stat-value">€4.1B+</div><div class="stat-label">欧盟 GDPR 累计历史罚款总额</div></div>
    </div>
</div>

<div class="card" style="margin-top:20px;">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-binoculars"></i> 核心市场驱动因素</h3></div>
    <div class="grid-2">
        <div>
            <h4>1. 严苛的监管执法力度</h4>
            <p style="font-size:0.9rem; color:var(--text-secondary);">欧盟 GDPR 针对数据泄露的最高罚款可达全球年营业额的 4% 或 2,000 万欧元（以较高者为准）。 regulatory agencies 强调了基础设施漏洞引发的数据泄露的法律责任。</p>
        </div>
        <div>
            <h4>2. CISO 与 DPO 协作融合</h4>
            <p style="font-size:0.9rem; color:var(--text-secondary);">企业管理层越来越意识到：没有网络安全就无法实现数据隐私。将安全漏洞与数据价值绑定是未来企业安全的必由之路。</p>
        </div>
    </div>
</div>
''')

pages_data["02-market-analysis/competitor-analysis.html"] = ("竞品分析", "02 市场分析", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-chess"></i> 竞品分析 (Competitor Analysis)</h1>
    <p class="page-subtitle">与 Tenable、Qualys、OneTrust、Vicarius 等行业头部厂商深度对比</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-table"></i> 核心竞品对比矩阵</h3></div>
    <div class="table-responsive">
        <table class="data-table">
            <thead>
                <tr>
                    <th>产品名称</th>
                    <th>CVE漏洞扫描</th>
                    <th>GDPR合规模块</th>
                    <th>漏洞与PII风险关联</th>
                    <th>无补丁/虚拟防护</th>
                    <th>部署模式</th>
                    <th>典型价格区间</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Tenable.io</strong></td>
                    <td><span class="badge badge-success">✓ 强 (VPR)</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-medium">~ 部分</span></td>
                    <td>SaaS / 混合云</td>
                    <td>$3,000 - $150,000/年</td>
                </tr>
                <tr>
                    <td><strong>Qualys VMDR</strong></td>
                    <td><span class="badge badge-success">✓ 强</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-success">✓ 包含</span></td>
                    <td>SaaS / Agent</td>
                    <td>$4,000 - $200,000/年</td>
                </tr>
                <tr>
                    <td><strong>OneTrust Privacy</strong></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-success">✓ 强 (DSAR/DPIA)</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td>SaaS</td>
                    <td>$10,000 - $300,000/年</td>
                </tr>
                <tr>
                    <td><strong>Vicarius vRx</strong></td>
                    <td><span class="badge badge-success">✓ 中</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-critical">✗ 无</span></td>
                    <td><span class="badge badge-success">✓ 无补丁防护</span></td>
                    <td>SaaS / Agent</td>
                    <td>$5,000 - $80,000/年</td>
                </tr>
                <tr style="background: rgba(15, 76, 129, 0.08); font-weight: bold;">
                    <td><strong>SGCS (SecureGuard)</strong></td>
                    <td><span class="badge badge-success">✓ 全面 (EPSS/KEV)</span></td>
                    <td><span class="badge badge-success">✓ 全面 (自动化)</span></td>
                    <td><span class="badge badge-success">✓ 独家关联引擎</span></td>
                    <td><span class="badge badge-success">✓ 自动生成WAF/虚拟补丁</span></td>
                    <td>混合云 / K8s / 多云</td>
                    <td>$15,000 - $120,000/年 (高ROI)</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
''')

pages_data["02-market-analysis/target-users.html"] = ("目标用户画像", "02 市场分析", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-users"></i> 目标用户画像 (Target User Personas)</h1>
    <p class="page-subtitle">关键决策者与日常使用者的需求与痛点分析</p>
</div>

<div class="grid-3">
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-user-shield"></i> CISO (首席信息安全官)</h3></div>
        <p><strong>痛点：</strong> 面对成千上万 CVE 漏洞，无法判断哪些真正威胁到含有客户 PII 数据的关键业务服务器。</p>
        <p><strong>需求：</strong> 基于业务上下文与隐私影响的漏洞优先级排序，自动化补丁防护与合规报告。</p>
    </div>
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-balance-scale"></i> DPO (数据保护官)</h3></div>
        <p><strong>痛点：</strong> 缺乏自动化技术工具证明企业基础设施符合 GDPR 第 32 条安全要求，处理 DSAR 繁琐。</p>
        <p><strong>需求：</strong> 实时 PII 敏感数据资产地图，72小时漏洞事件响应证据链与自动化 DPIA 评估。</p>
    </div>
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-laptop-code"></i> SecOps / DevOps 工程师</h3></div>
        <p><strong>痛点：</strong> 漏洞修复任务繁重，打补丁可能导致生产服务中断，工单与 Jira/ServiceNow 割裂。</p>
        <p><strong>需求：</strong> 一键生成 WAF 虚拟补丁规则，自动化工单对接与修复效果校验闭环。</p>
    </div>
</div>
''')

# Section 03: Product Vision
pages_data["03-product-vision/vision-mission.html"] = ("愿景与使命", "03 产品愿景与定位", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-bullseye"></i> 愿景与使命 (Vision & Mission)</h1>
    <p class="page-subtitle">SGCS 平台的长期发展目标与核心信念</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-eye"></i> 产品愿景 (Vision)</h3></div>
    <p style="font-size: 1.1rem; line-height: 1.8;">成为全球中大型跨国企业首选的<strong>安全漏洞与隐私合规一体化数字信任基础设施</strong>，让企业在遵守严格数据法规的同时，轻松抵御系统漏洞威胁。</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-rocket"></i> 产品使命 (Mission)</h3></div>
    <p style="font-size: 1.1rem; line-height: 1.8;">打破网络安全与法律合规之间的屏障，通过智能化的技术关联与自动化工作流，赋能 CISO 和 DPO 实现“事前预防-事中防护-事后可追溯”的无缝安全合规保障。</p>
</div>
''')

pages_data["03-product-vision/core-problems.html"] = ("核心问题定义", "03 产品愿景与定位", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-exclamation-triangle"></i> 核心问题定义 (Core Problems Defined)</h1>
    <p class="page-subtitle">企业在漏洞管理与 GDPR 合规中面临的三大核心阻碍</p>
</div>

<div class="grid-3">
    <div class="card">
        <h3>1. 风险优先级失控</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">安全团队每天面对成百上千个 CVE 漏洞，传统 CVSS 评分仅衡量技术危害，忽略了被攻击系统是否存储有 GDPR 保护的客户个人敏感数据 (PII)。</p>
    </div>
    <div class="card">
        <h3>2. 合规举证与响应滞后</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">GDPR 要求违规或高危漏洞事件必须在 72 小时内报告监管机构，而传统依靠 Excel 和人工排查的方式往往需要数周才能完成举证与影响评估。</p>
    </div>
    <div class="card">
        <h3>3. 补丁打不上与业务中断风险</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">遗留系统或关键业务无法立即重启安装 Patch，安全团队缺乏无需修改代码的“无补丁虚拟防护（Patchless Protection）”手段。</p>
    </div>
</div>
''')

pages_data["03-product-vision/value-proposition.html"] = ("核心价值主张", "03 产品愿景与定位", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-gem"></i> 核心价值主张 (Value Proposition)</h1>
    <p class="page-subtitle">SGCS 为企业带来的三大突破性核心价值</p>
</div>

<div class="grid-3">
    <div class="card">
        <div class="stat-icon primary" style="margin-bottom:12px;"><i class="fas fa-network-wired"></i></div>
        <h3>1. 漏洞与 PII 风险智能关联</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">行业首创风险融合算法，根据 CVE 漏洞严重度 + PII 数据敏感度动态计算“隐私风险暴露值”，帮助团队优先修复影响核心数据的漏洞。</p>
    </div>
    <div class="card">
        <div class="stat-icon success" style="margin-bottom:12px;"><i class="fas fa-shield-virus"></i></div>
        <h3>2. 无补丁虚拟防护 (Patchless Protection)</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">针对无法立即停机修复的系统，一键生成 WAF 防护规则或虚拟补丁，在不破坏生产环境的前提下实时阻断 CVE 漏洞攻击。</p>
    </div>
    <div class="card">
        <div class="stat-icon high" style="margin-bottom:12px;"><i class="fas fa-award"></i></div>
        <h3>3. 自动化 GDPR 审计证据链</h3>
        <p style="font-size:0.9rem; color:var(--text-secondary);">全流程记录扫描、风险排序、修复与验证历史，并带有时钟与区块链防篡改签名，一键输出符合 DPA 审计要求的完整证据包。</p>
    </div>
</div>
''')

print("Section 01-03 generated in dictionary.")
