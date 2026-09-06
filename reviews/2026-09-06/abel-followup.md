# 跟进独立复核：abel-followup

日期：2026-09-06。保留报告原文，复核范围及剩余事项按正文。

**五类修订均妥当，首轮数学异议可以关闭；未发现这些修订引入新的证明问题。** 本轮仅核对修订差异、相关上下文及 Hardy 页码，未重跑脚本或重新审查未改动的主链。

| 修订 | 闭环意见 |
|---|---|
| [massfloor 量词](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:634) | 已明确固定 \(\sigma\)、\(Y_j\to\infty\)、有限整数 \(N_j\ge Y_j\)、非零质量及固定预算常数。原先固定 \(N=2\) 的反例已被正确排除，关闭。 |
| [摘要截断规则](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:28) | 整数截断与 \(N=\lfloor\Phi(Y)\rfloor\)、\(\Phi\) 最终连续非减已与正文一致，关闭。 |
| [实解析性](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:278) | \(\Re z>0\) 上局部一致支配给出全纯性，再经 \(z=1/Y\) 得到实解析性，论证充分，关闭。 |
| [复现说明](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:784) | 命令、\(N=40Y\)、48个样本、软件版本及浮点误差边界均与首轮实际复跑一致，关闭。 |
| [外部输入说明](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:769) | Hardy 原始引用及 FKS 作为定性 PNT 来源均合适。FKS 给出 \(\psi(x)\sim x\)，结合初等的 \(\psi(x)-\vartheta(x)=O(\sqrt{x}\log^2x)\)，即可得到所用素数区间质量下界，无循环性。 |

**Hardy 的印刷页码 1012–1014 正确。** 第1012页开头陈述临界线上存在无穷多个零点，第1014页完成反证，随后开始另一篇文章。[第1012页原文转录](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1014)、[第1014页原文转录](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1016)。

Gallica 地址中的 `f1014` 是数字化图像序号，不能直接解释为印刷第1014页。本轮该直链未成功读取，因此**书目页码已核实，Gallica 链接的实际落页尚待下载后核对**。另可将[首次使用处第134行](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:132)的 `\cite{DLMF}` 同步为 `\cite{Hardy,DLMF}`；这是引用位置完善，不再构成证明缺口。

可归档的简短范围比较：

> Mahatab–Mukhopadhyay 重述并发展 Mellin–Landau 振荡机制；Montgomery–Vaughan 提供一般有限指数和的局部间距均值估计；FKS 提供 \(\psi(x)-x\) 的定量上界。本文将这些输入用于指定的、保留质量中心项的双通道 Brownian 响应，推导截断一致下界及连续实尺度上的质量预算障碍。所核读定理没有直接陈述本文这个归一化响应的完整结论，但这不足以证明组合的新颖性；“internally audited technical reconstruction / no priority claim”的定位合适。[MM v4](https://arxiv.org/html/1512.03144v4)、[MV 原文](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)、[FKS v3](https://arxiv.org/pdf/2204.02588v3)。

还剩一项**归档状态用语**：[第809–811行](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:809)已经写成 “are archived in research note 308”。本轮文件清单中尚未出现 note308，与“正在编写”一致。该完成式应在实际落盘后保留，或暂改为进行式；它不影响数学闭环。

本轮所核源稿 SHA-256：`3905683F66589DED2EFBAC5EDFDC8A28F11EC3619980CCBAFC55B95CE3B05CA1`。全程只读，未修改、提交或推送文件；文献下载及归档完成状态未由本轮认证。
