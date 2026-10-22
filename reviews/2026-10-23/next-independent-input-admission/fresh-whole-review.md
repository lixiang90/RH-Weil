# 算术 theta 来源门的独立整稿 fresh 审查

2026-10-23。独占审查；不改根稿、STATE、cadence或合同，不新增数学轮。

**结论：限定 PASS；本次只能作为来源0消费，不能作为新独立容量或新数学合同。**
审查对象是[根部综合稿](../../../goals/reviews/2026-10-23-arithmetic-theta-capacity-source-admission.md)及同目录三独占分支。
恢复时读 README／STATE、Goal、C041、frontier及D20261022N，运行research_state check后show；核实际工作树。
最新数学仍578；最强旧 whole 后果仍为542＋555→557的leading4/5负惯性上预算。
本稿不重审所有历史证明，也不重证KRY全部CM局部变形来源；核查限于下列实际消费箭头。

## 1. 原件、规范与唯一必要修正

直接读取[作者Bonn原件](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)的导言Theorems1–3、§1的(1.4)、§4的Lemmas4.1–4.2及(4.11)–(4.13)。
Theorem2确实给根稿(1)的mixed完成化身份；经典因子为
\(\pi^{-s/2}\Gamma(s/2)\zeta(s)\)，另一因子为odd quadratic completion且未吸入导子幂。
因此“此来源完全没有经典Γ”的排除理由不成立。常数项扣除的Mellin变换及其原安全域必须同时保留。

首次出稿漏写一个实质假设：这里的q须为**素数**，除q>3及q≡3 mod4以外不能省略。
已向root指出；root和capacity分支均已补该限定。此处不消费一般复合判别式推广。

## 2. Γ半因子、全部powers与signed逆的方向

自行按对数求导与标准digamma积分核得

\[
\tfrac12[\psi((s+1)/2)-\psi(s/2)]
=\int_0^\infty\frac{e^{-su}}{1+e^{-u}}\,du.
\]

根稿半因子准确；积分Re s>0收敛，Euler和须Re s>1。
\((1-\chi(n))\Lambda(n)\)保留全部proper powers及ramified q，不是只保一次素数。
差Γ核在原点有界，说明奇性在相减中抵消；这不能推出单独完整Weil Γ的正号。
原件实际给的是Schwartz→induced section及线性degree身份，未给全物理r的primitive Hermitian自交。

在split、inert与ramified位，有限Euler逆依次含负的一次、二次和一次系数。
对单位Dirichlet质量的像已非正，足以否定“该解卷积自动保正测度”的推理。
这没有证明实际CM输入经专门signed相消后必负，也没有给实际源必须支付的norm lower；
Γ因子的逆及全源费用仍未付款。根稿准确保留了这些限制，没有将一条线性degree身份提升成正极化。

## 3. 幂图、原费用与absolute／relative边界

对\(\mathfrak S=\mathbf P^1_{\mathbf Z}\times\mathbf P^1_{\mathbf Z}\)，
\(F_1=\{y=\infty\},F_2=\{x=\infty\}\)，直接看函数y−xⁿ的零极点，确有

\[
\operatorname{div}(y-x^n)=\Gamma_n-F_1-nF_2.
\]

故F₁/F₂方向及Γₙ交数与567一致；无额外整p-fibre除子分量。
n=pᵏ时p-fibre是实际不可分Frobenius图，但primitive类仍为0。
有限N的cell积分对全S_exp合法，复源应先取实循环系数再复化；
\(\|a(r)\|_1\le\sqrt{2L}\|r\|_{du}\)只在固定支撑窗成立，
全线只报L¹强源费用。它不是Green／height／jet费用，外侧无界cell也无全线du读出界。
零primitive map确实消全405且杀537；这只是该具体模型的coverage失败。
模型总维为3，根稿未误称算术曲面，也未排正亏格、nonprincipal metric及有费无限完成。

574的unitary absolute二阶类经周期unitary gauge可平方平凡；
tensor双线性的实absolute pairing因此消该类。保两边界frame时所需gauge不为1，
relative类并非二阶，不能沿用这个零结论。两对象及失败范围在根稿／分支中已严格分开。

## 4. 连续反测与函数域来源

连续例的B_g须按d分别解释。对g=uφ，φ非零非负偶且支撑于(−1,1)，有

\[
B_{g,d}=\begin{cases}
\displaystyle\int u\varphi(u)\,\frac{\sin(\sqrt d\,u)}{\sqrt d}\,du,&d>0,\\
\displaystyle\int u\varphi(u)\,\frac{\sinh(\sqrt{-d}\,u)}{\sqrt{-d}}\,du,&d<0.
\end{cases}
\]

d=±1/16时两者各自严格正，毋须相等。
积分分部给\(a_{(D^2-1/4)g}=-(d+1/4)a_g\)，故
\(Q_d(r)=2d(d+1/4)^2B_{g,d}^2\)严格异号，双pole矩为0。
这是574旧例的准确具体化，不是一个新反模型。
外加的P¹模型在两例均给0，所反驳的是比较identity；两例并未被证明满足KRY几何输入。

函数域的可消费来源仍是同一C×C上的RR、有效截面乘法和固定容量，先给primitive Hodge负号，
再由全部Frobenius图mixed交数给全Weil正性；proper powers、H⁰/H²极点与aliases保留。
CM有效0-cycle的线性degree不能替代这条二次链，也不能用两个不同对象各自正号拼接为一份同源证书。

## 5. 净后果、计轮及停止范围

核557原式，whole预算的准确方向为
\(n_-(Q_L)\le B_{\rm mix}(L)\)、\(\log B_{\rm mix}(L)/e^L\to4/5\)。
它不提供实际负谱lower；本次也没有改进该最强旧后果。
560与577的两个exact remainder尚无运输身份，不能互相抵费。
405全noncompact主关系、537非根、全complex原du／zero-extension Dlog、完整Γ/contact、全部幂和双pole均未删。
没有新fixed-source q费、D′消失或成长L统一控制；553的全线连续map障碍也未被theta名称绕过。

因此来源审计、旧principal／torsion的直接具体化及fresh各计0；不建C042/579。
cadence1、历史42、formalcycle15及长期Goal完成门保持；独立容量／whole／core／coupling／Ξ瓶颈未改。
新信息仅是定位真实mixed完成化来源及把未付箭头收窄到signed运输／同源primitive比较。
停止此直接抽取与旧廉价载体方案，不把局部失败写成整个theta或relative方法类不可能。
只有实际新source公式或signed identity连同405／537、原费用、局部过滤及容量系数，才可重新准入。

## 6. 最终版本绑定

已在两分支修后复核本地LF规范SHA256：

| 被审文件 | LF SHA256 |
|---|---|
| root综合稿 | `f668e98fd005d9063448ef260dc12dce5ded119f2c0fcd022085f77d7598e04f` |
| capacity分支，prime q已补 | `51bc4de0ad018b81f5968ad2390feb3d1fb1cd6dfe397b9aecd906ab6c4b4be8` |
| function-field分支，B_g两号定义已补 | `a29a070f808853f8cdbe6571d747266bcd2ef990e188dd56bf0b825a8510cd7b` |
| strongest-old分支 | `43f8d2eb5009e3698119acb271b7407b036f7f47460902fe7636cee958edbb60` |

root随后仅可将“待fresh／尚未结算”的首段状态更新为fresh及root消费已完成；
这项status-only改动不改变上述数学审查范围。若数学陈述、量词、方向或停止范围再变，须重开相应前件。
