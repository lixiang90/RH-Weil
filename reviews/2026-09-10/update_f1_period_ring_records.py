"""Record the reviewed finite-level stop and the new period-ring candidate.

One-time migration; preserve existing line endings and the exact long-term criteria.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = ROOT.parent

def replace(path, old, new):
    raw = path.read_bytes()
    newline = b"\r\n" if b"\r\n" in raw else b"\n"
    encode = lambda s: s.encode("utf-8").replace(b"\n", newline)
    assert raw.count(encode(old)) == 1, (str(path), old[:70])
    path.write_bytes(raw.replace(encode(old), encode(new)))

def append(path, value):
    raw = path.read_bytes()
    newline = b"\r\n" if b"\r\n" in raw else b"\n"
    path.write_bytes(raw + value.encode("utf-8").replace(b"\n", newline))

snapshot = WORKSPACE / "archive/GOAL.20260909.f1-periodic.md"
assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == "d3e4bfecdfd18507cbe92e0579ce6f6c44d7fd83211a0914fc80167e7abbafd5"
goal = WORKSPACE / "GOAL.20260909.md"
assert goal.read_bytes() == snapshot.read_bytes()
replace(goal,
"""下一具体输入是H_p结构子层、单位Jensen及主除子／线性系统比较，
[369草案](RH-Weil/notes/369-f1-hp-solenoid-unit-slope.md)尚未独立审核，不计入已审基线。
整个算术平方、交叉及RR仍开放；字符族层不预设等同原文Witt完备化层。
这些局部比较和已知机制重建不触发第十节C。""",
"""[369](RH-Weil/notes/369-f1-hp-solenoid-unit-slope.md)已完成H_p子层及完整纤维带上单位斜率的独立复核。
[370](RH-Weil/notes/370-f1-finite-level-periodic-meromorphic-rigidity.md)证明所选局部有限层复函数类别
的周期商全局亚纯函数只有常数，其直接承担周期RR的候选停止。
[371](RH-Weil/notes/371-f1-tate-curve-frobenius-weight.md)区分复Tate平移、算术权重与Witt Frobenius；
370–371均已独立复核，排除范围不外推到全部F₁几何。
当前主问题转到[372](RH-Weil/notes/372-f1-period-ring-tropical-principal-comparison.md)：
使用实际完备period ring、权一元素及同权分式构造热带主除子，并核查其Proj几何身份。
该稿当前待独立复核；审核后刻画比较像、一般非代数闭底域的除子／截面接口，
优先给实际可容许线性系统的新输入。不得把所选域的H_p值群结果与代数闭域定理混用。
路线修订前原始字节已存[周期比较快照](archive/GOAL.20260909.f1-periodic.md)。
整个算术平方、交叉、固定ζ相对迹及RR仍开放；不由已知FF理论自动导入。
本批局部比较与机制重建尚不触发第十节C；第十节B/C保持原文。""")
boundary = "### B. 较远期目标方向".encode()
assert goal.read_bytes().split(boundary, 1)[1] == snapshot.read_bytes().split(boundary, 1)[1]
append(WORKSPACE / "archive/README.md", """

- [GOAL.20260909.f1-periodic.md](GOAL.20260909.f1-periodic.md)：2026-09-10完成369–371复核、
  将当前主问题转入实际period ring主除子比较前的原始字节。有限层周期亚纯刚性阻止直接移植RR，
  新来源提供可检验的同权分式构造。SHA256：
  `d3e4bfecdfd18507cbe92e0579ce6f6c44d7fd83211a0914fc80167e7abbafd5`。
  第十节B/C保持原文；快照链接保留原根目录语境，Git镜像仅重定位链接。
""")
replace(ROOT / "scripts/sync_goal.py", '    "GOAL.20260909.md",', '    "GOAL.20260909.md",\n    "archive/GOAL.20260909.f1-periodic.md",')
replace(ROOT / "scripts/sync_goal.py", 'if relative.startswith("archive/GOAL.20260906"):', 'if relative.startswith(("archive/GOAL.20260906", "archive/GOAL.20260909")):')

replace(ROOT / "README.md",
"""以上三项已完成独立内部复核；[369](notes/369-f1-hp-solenoid-unit-slope.md)为下一子层修复的未审草案。
所选字符族结构层与完整算术平方／RR的比较仍开放。""",
"""366–369均已独立内部复核。[370](notes/370-f1-finite-level-periodic-meromorphic-rigidity.md)
证明所选有限层复函数周期商的亚纯刚性；[371](notes/371-f1-tate-curve-frobenius-weight.md)
核查复Tate模型与Frobenius权重，两项复核闭环。
当前[372](notes/372-f1-period-ring-tropical-principal-comparison.md)从实际完备period ring
构造同权分式及非零热带主除子，正在独立复核；完整算术平方／RR及固定ζ接口仍开放。""")
replace(ROOT / "RESEARCH_BRANCHES.md",
"""| 当前主线 | F1-EX1：366–368的整族主除子、实际p周期线丛及[theta／系数障碍](notes/368-f1-tropical-theta-and-coefficient-obstruction.md)已独立复核；[369](notes/369-f1-hp-solenoid-unit-slope.md)推进H_p子层及单位斜率，当前未审 | 固定ζ及比较要求；周期对象不等于完整算术平方，全Q频率不能直接接入原文H_p结构层／RR |""",
"""| 当前主线 | F1-EX1：[369](notes/369-f1-hp-solenoid-unit-slope.md)单位斜率、[370](notes/370-f1-finite-level-periodic-meromorphic-rigidity.md)有限层周期亚纯刚性、[371](notes/371-f1-tate-curve-frobenius-weight.md)权重边界均已复核；[372](notes/372-f1-period-ring-tropical-principal-comparison.md)构造实际period ring同权分式及热带主除子，当前待复核 | 停止所选有限层复模型直接RR候选；审查完备化、relative Frobenius及一般F几何身份，继而刻画像和可容许线性系统。固定ζ接口仍缺 |""")

next_path = ROOT / "goals/NEXT.20260909.md"
replace(next_path, "## 下一具体输入：周期线性系统的系数与主除子比较", "## 已完成的周期比较与候选停止范围")
replace(next_path,
"""下一任务为构造保留H_p的结构子层及真实轨道上的拉回比较，
检验局部化、T_mu与周期下降封闭，并单独证明其单位的Jensen斜率在H_p。
若这些成立，再推进主除子／torsion与可容许线性系统的比较。
不得仅从有效除子的逐对象提升导入热带RR，更不能由周期RR替代G8b或完整算术平方。

后续[369证明草案](../notes/369-f1-hp-solenoid-unit-slope.md)提出G_p因子、
实际G轨道的拉回与单位Jensen斜率引理；当前未审，尚未计入已完成输入。
详见[下一证明计划](../reviews/2026-09-10/f1-hp-next-proof-plan.md)。""",
"""[369](../notes/369-f1-hp-solenoid-unit-slope.md)完成G_p因子、拉回与完整纤维带上的单位斜率；
只读复核通过，未扩大为所有非单位或任意开集的比较定理。
[370](../notes/370-f1-finite-level-periodic-meromorphic-rigidity.md)证明有限层类别周期商
的全局亚纯函数只有常数，线丛截面维数至多一，不能直接承担预期周期RR。
[371](../notes/371-f1-tate-curve-frobenius-weight.md)排除用复Tate平移直接实现算术p权重；
这些停止范围均已独立复核，不排除不同结构层或非阿基米德来源。

## 当前有限主问题：实际period ring的主除子与截面接口

[372](../notes/372-f1-period-ring-tropical-principal-comparison.md)使用值群H_p的实际perfectoid F，
完成环B及Ψ_f(y)=−y v_(1/y)(f)，显式构造φ(F_a)=pF_a和同权分式。
当前待独立复核；已保存上游Lecture6／8／11／19原PDF。

1. 审核紧区间轮廓稳定性、作用类型、双向级数、theta恒等式及非零主除子。
2. 核查同权分式的Proj有理函数身份；一般F与代数闭F的定理前提分开。
3. 刻画可实现的热带主除子像，再检验局部重数、线性系统及更一般系数的可容许扩展。
   成功要求函数／截面层面的实际比较；只匹配次数不足。
4. 该模型若不能覆盖所需参数，精确记录阻碍并切换扩展机制，不改低G0–G8的要求。

不得从逐对象有效除子提升导入完整RR；一般F的几何比较及固定ζ相对迹仍是开放输入。
整个Goal保持active；372的局部构造即使复核通过，也不自动达到第十节C。
""")

replace(ROOT / "goals/PROGRESS.md", "## 以下为先前阶段记录", """## 2026-09-10续轮：有限层刚性与period ring主除子

369经Gibbs复核通过，修正Haar归一化及有限代数的A_p∩S范围。
370经Gibbs复核：局部有限层复函数的周期商全局亚纯函数只有常数；
这是明确类别的停止结果，不是全F₁路线障碍。
371经Singer复核：复Tate平移的p作用为恒等，不能直接承担目标除子的p权重；
已修正平移／群幂、f^p／φ(f)=pf、乘法／加法和不同完成环的区别。

372给完备period ring的轮廓变换Ψ、显式权一元素和非零热带主除子，当前待独立复核。
来源辅助已确认同权比值可直接成为Proj上的实际有理函数；
Lecture19全局截面同构使用代数闭前提，未直接搬到当前H_p值群的F。
新保存四讲PDF共17页；2018 Jessen的2π归一化与2026 §§3–5的核读范围单列。
Jessen–Tornehave原PDF获取HTTP500，登记链接及失败，未称已归档／核审全文。

GOAL当前执行段已据此修订，修订前原件SHA256
d3e4bfecdfd18507cbe92e0579ce6f6c44d7fd83211a0914fc80167e7abbafd5已归档；
第十节B/C原始字节保持。下一动作见任务单；当前批次提交及远程保存待实际核验后补记。
尚无RH、比例、非零区域或完整RR结论，Goal继续active。

## 以下为先前阶段记录""")

manifest_path = ROOT / "literature/manifest.json"
manifest = json.loads(manifest_path.read_bytes())
downloads = json.loads((ROOT / "reviews/2026-09-10/f1-lurie-source-download.json").read_bytes())
titles = {
    "06": ("Lecture 6: Definition of the Fargues-Fontaine Curve", "2018-10-29", "全讲4页核读；环、全族Gauss范数完成及Frobenius定义。未由此宣称完整曲线理论认证。"),
    "08": ("Lecture 8: The Field BdR", "2018-10-29", "Singer完整核读5页；一般F的untilt/DVR输入、Remark7才追加代数闭，尚无完整零点重数比较。"),
    "11": ("Lecture 11: Trivial Eigenspaces of the Frobenius", "2018-10-31", "全讲4页核读；P5、P8、C9–12的完成Gauss轮廓稳定性及φ关系；PDF3页渲染核对。"),
    "19": ("Lecture 19: Line Bundles on the Fargues-Fontaine Curve and Their Cohomology", "2018-11-18", "Singer完整核读4页；全讲代数闭前提、Construction1、Theorem5的截面同构及其限制。")
}
for entry in downloads:
    number = entry["id"][-2:]
    title, date, scope = titles[number]
    entry["title"] = title
    entry["version"] = "Math 205 Fall 2018; PDF dated " + date + "; IAS author copy archived 2026-09-10"
    entry["status"] = "外部背景；" + scope
    entry["review_note"] = "../reviews/2026-09-10/f1-lurie-geometric-binding-source-audit.md" if number in ("08", "19") else "../notes/372-f1-period-ring-tropical-principal-comparison.md"
    assert not any(e["id"] == entry["id"] for e in manifest["entries"])
    manifest["entries"].append(entry)

for entry in manifest["entries"]:
    name = entry.get("file")
    if name == "f1/cc-complex-lift-1805.10501v1.pdf":
        entry.setdefault("reading_updates", []).append({"date": "2026-09-10", "scope": "新增PDF23–31页核读；24、29页渲染。核查(22)/(23)/(29)的2π归一化，保留p周期下降与RR缺口。", "review_note": "../reviews/2026-09-10/f1-jessen-normalization-source-audit.md"})
    if name == "f1/cc-absolute-geometry-2606.06604v1.pdf":
        entry.setdefault("reading_updates", []).append({"date": "2026-09-10", "scope": "Singer核读§§3–5(PDF11–30)，区分点集／拓扑分类、复Tate曲线及展望中的B^{φ=p}下降；未重审全部FF理论。", "review_note": "../reviews/2026-09-10/f1-2026-period-ring-source-audit.md"})
manifest["entries"].append({
    "id": "Jessen-Tornehave-1945", "category": "f1-background", "authors": "Børge Jessen; Hans Tornehave",
    "title": "Mean motions and zeros of almost periodic functions", "version": "Acta Mathematica 77 (1945), 137–279",
    "source_url": "https://archive.ymsc.tsinghua.edu.cn/pacm_paperurl/20170108203121071731656",
    "pdf_url": "https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5656-11511_2006_Article_BF02392225.pdf",
    "doi": "10.1007/BF02392225", "download_status": "failed", "attempted_on": "2026-09-10",
    "status": "原PDF经代理与直接连接HTTP500；出版方返回订阅HTML。无本地PDF；未核读原始全文。"
})
manifest["scope"] += "; 2026-09-10：实际period ring、FF几何前提及Jessen归一化来源"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
append(ROOT / "literature/README.md", """

## 2026-09-10：period ring、FF几何与Jessen归一化

2026固定原件新增核读§§3–5，见[来源审查](../reviews/2026-09-10/f1-2026-period-ring-source-audit.md)。
2018固定原件新增核读PDF23–31页；(22)/(23)/(29)之间的2π归一化用显式函数核对，
见[Jessen审查](../reviews/2026-09-10/f1-jessen-normalization-source-audit.md)。这些不扩大为全文数学认证。

以下均为Jacob Lurie的Math 205（Fall 2018）讲义，由[作者IAS目录](https://www.math.ias.edu/~lurie/205.html)
下载原件；四份共17页，全页解析通过，SHA256和获取时刻见manifest及
[下载记录](../reviews/2026-09-10/f1-lurie-source-download.json)。作者讲义不是本项目的新理论。

| 原件 | 日期／页数 | 本轮使用及范围 |
|---|---|---|
| [Lecture 6: Definition of the Fargues-Fontaine Curve](f1/lurie-2018-lecture06.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture6-Curve.pdf) | 2018-10-29／4 | B及Gauss范数完成、Frobenius；全讲核读 |
| [Lecture 8: The Field BdR](f1/lurie-2018-lecture08.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture8-BdR.pdf) | 2018-10-29／5 | 一般F的untilt、局部DVR及代数闭前提边界；Singer全讲核读 |
| [Lecture 11: Trivial Eigenspaces of the Frobenius](f1/lurie-2018-lecture11.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture11-TrivialEigenspaces.pdf) | 2018-10-31／4 | P8及C9–12的完成轮廓稳定性；全讲核读，PDF3页渲染 |
| [Lecture 19: Line Bundles on the Fargues-Fontaine Curve and Their Cohomology](f1/lurie-2018-lecture19.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture19-LineBundles.pdf) | 2018-11-18／4 | 全讲假定F代数闭；Theorem5不可直接搬到372的F，Singer全讲核读 |

[几何接口审查](../reviews/2026-09-10/f1-lurie-geometric-binding-source-audit.md)区分实际Proj有理函数、
完整截面同构与尚缺的除子重数比较；[372](../notes/372-f1-period-ring-tropical-principal-comparison.md)
的热带比较另有本项目证明，当前待独立复核。

**Jessen–Tornehave（1945）**，*Mean motions and zeros of almost periodic functions*，
Acta Math.77,137–279；[DOI](https://doi.org/10.1007/BF02392225)／
[YMSC目录](https://archive.ymsc.tsinghua.edu.cn/pacm_paperurl/20170108203121071731656)。
本轮PDF获取HTTP500，未保存有效原件，也未核读原始全文；失败状态已列manifest。
""")
print("Updated current research records; long-term GOAL bytes preserved.")
