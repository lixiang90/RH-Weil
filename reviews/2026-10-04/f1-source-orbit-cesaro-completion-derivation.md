# 真源轨道的Cesàro范数极限与完成后的非紧固定点

2026-10-04。独立推导，保留[430](../../notes/430-f1-source-stable-periodic-smoothing-algebra.md)的原u、原c与 \(d=d_q\)、实际V及 \(G_M\) 周期光滑有限传播核类。本报告只写新研究，不改旧笔记。关键结果是原轨道平均具有显式算子范数收敛速度；通常得到真实非紧源固定点。因此[431](../../notes/431-f1-source-orbit-essential-symbol-and-boundary-injectivity.md)的有限支持单射性不能外推到范数完成。

## 1. 原纤维中的源角列及统一Young界

使用430的完整Hilbert酉坐标 \(x=t-jL-kM\)。源角e在每个q块的单位向量为
\[
 c_k(x)=\sum_jc(x+jL+kM)e_{j,k},\qquad \|c_k(x)\|=1,
\]
原v将 \(c_k\) 移到 \(c_{k+1}\)，u在源补空间恒等。记源角等距嵌入 \(J_x:\ell^2(\mathbb Z)\to\mathcal H_0\)，\(J_xe_k=c_k(x)\)。V在此表示中为向量值乘法 \(z(x)\)。其源角部分准确为
\[
 (eV\phi)(x)=J_x a(x)\phi(x),\qquad
 a_k(x)=\delta_{k0}a_p(x)+\mathbf1_{k<0}f(x+kM),             \tag{1}
\]
其中 \(a_p=\sum_{j<0}c(x+jL)^2\)，\(f=cd\)。这包含实际负q行与p边在源角内的分量，不是任意轨道模型。

\(0\le a_p\le1\)，f紧支，因此任意x的非零 \(f(x+kM)\) 数目有统一有限上界K。例如可取 \(K=2+\lceil\operatorname{diam}(\operatorname{supp}f)/M\rceil\)，f=0时该部分直接为零。故
\[
 \sup_x\|a(x)\|_{\ell^1}\le C:=1+K\|f\|_\infty<\infty.     \tag{2}
\]
令 \(E_j=u^jeV\)，则纤维上 \(E_j(x)=J_x S^j a(x)\)，S为q链的双边移位。对任何有限标量序列λ，Young不等式给
\[
 \left\|\sum_j\lambda_jS^ja(x)\right\|_{\ell^2}
       \le\|a(x)\|_{\ell^1}\|\lambda\|_{\ell^2}.
\]
因此实际列算子
\[
 Y_N=(E_1,\ldots,E_N):L^2(\mathbb R)\otimes\mathbb C^N\to\mathcal H
 \quad\text{满足}\quad\boxed{\|Y_N\|\le C\ \text{对所有N}.} \tag{3}
\]
这里是对移动源角eV的统一界。全V轨道另含不动分量，其无限Gram一般无统一界；两者没有混同。

## 2. 任意有界时间B的精确范数平均

置 \(F=(1-e)V\)，则 \(uF=F\)，且
\[
                         u^jV=F+E_j.                      \tag{4}
\]
对任意 \(B\in\mathcal B(L^2(\mathbb R))\)，定义实际有限平均
\[
 \mathcal M_N(B)=\frac1N\sum_{j=1}^Nu^jVBV^*u^{-j}.
\]
展开(4)得到
\[
 \mathcal M_N(B)=FBF^*+
  \frac1N\big(FB\sum_jE_j^*+(\sum_jE_j)BF^*\big)
  +\frac1N Y_N(I_N\otimes B)Y_N^*.                         \tag{5}
\]
令 \(D_N\phi=(\phi,\ldots,\phi)\)，\(\|D_N\|=\sqrt N\)，则 \(\sum_jE_j=Y_ND_N\)，范数至多 \(C\sqrt N\)。最后一项范数至多 \(C^2\|B\|/N\)。所以
\[
 \boxed{\ \|\mathcal M_N(B)-FBF^*\|
 \le\frac{2\|F\|\|B\|C}{\sqrt N}+\frac{C^2\|B\|}{N}
                      \longrightarrow0.\ }               \tag{6}
\]
此处无需B正、周期、平滑或有限传播；它是指定种子 \(VBV^*\) 及真实u的完整有界算子范数结论。没有据此给任意 \(\mathcal B(\mathcal H)\) 元素构造一个全局Cesàro条件期望。

若 \(B\in G_M\)，每项平均属于430的实际源稳定域，故极限属于该域的算子范数完成。任意有界B不必属于G_M；其范数极限虽合法，不自动准入这个特定完成。

## 3. 固定点的准确Gram与周期端

\(uF=F\) 直接给
\[
                         u(FBF^*)u^*=FBF^*.                \tag{7}
\]
原源角／补空间正交分解给
\[
 F^*F=M_\nu,\qquad
 \nu=a_p+a_q-a_p^2-z_0,\qquad
 z_0(x)=\sum_{k<0}f(x+kM)^2.                               \tag{8}
\]
\(\nu\ge0\)，充分负端为0，充分正端为
\[
 w(x)=1-\alpha(x),\qquad
 \alpha(x)=\sum_{k\in\mathbb Z}c(x+kM)^2d(x+kM)^2.          \tag{9}
\]
\(w\) 为光滑M周期函数，\(0\le w\le1\)。它是原不动源补空间在正时间端的实际质量，不是为目标周期权重选择的修正。

## 4. w非零时的实际非紧固定算子

取任意非零 \(g\in C_c^\infty\)，\(g^*(s)=\overline{g(-s)}\)，令
\[
 h=g*g^*,\qquad B=U(h)=U(g)U(g)^*\ge0,
 \qquad h(0)=\|g\|_2^2>0.                                 \tag{10}
\]
B属G_M。若w非零，取小区间I使 \(w\ge\epsilon>0\)，并使任意 \(x,y\in I\) 都满足 \(\operatorname{Re}h(x-y)>h(0)/2\)。选非负非零 \(\psi\in C_c^\infty(I)\)。则
\[
 \langle w\psi,U(h)w\psi\rangle>0.                         \tag{11}
\]
这是完整卷积核的正实部积分；B为正，自身内积真实非负，并且上述选择使其严格正。

令 \(\psi_n=\mathsf T_{nM}\psi\)，n充分大时其支集在 \(\nu=w\) 的正端。置
\[
 \xi_n=F\psi_n/\|\sqrt w\psi\|_2.
\]
这些为单位弱零向量：\(F\) 有界、紧支向量右移弱趋零，且(8)及周期性使分母精确为其范数。对 \(X=FU(h)F^*\ge0\)，
\[
 \langle\xi_n,X\xi_n\rangle
   =\frac{\langle w\psi,U(h)w\psi\rangle}{\|\sqrt w\psi\|_2^2}
   =:\kappa>0                                             \tag{12}
\]
对所有充分大n相同。Cauchy–Schwarz给 \(\|X\xi_n\|\ge\kappa\)，紧算子不能如此，故X非紧。它又是(7)的真实固定点，且由(6)属于范数完成。

因此431的有限支持迹类商单射性不延伸到该完成的Calkin商。该固定点不在原有限支持域：若在域内且非迹类，431将强制其共轭差非紧，而(7)的差为零。无限平均和有限词是不同的实际准入。

## 5. p小于q时的统一非零判据

直接在一周期积分并换元，
\[
 \int_0^M w(x)\,dx=M-\int_{\mathbb R}c(t)^2d(t)^2dt.
\]
平方分割使 \(d^2\le1\)，\(\int c^2=L\)，因此
\[
                  \boxed{\int_0^M w\ge M-L.}              \tag{13}
\]
若 \(p<q\)，则 \(L<M\)，w对**每个**原合法c、d都非零。因此上节非紧固定点不依赖特选分割或浮点素数认证。若 \(p>q\)，此界不强制w非零，应检查实际(9)，不能反过来宣布w必为零。

## 6. w恒零时的平滑核限制

若 \(w\equiv0\)，(8)使ν两端都为0，故 \(\nu\) 光滑紧支。取光滑紧支χ在 \(\operatorname{supp}\nu\) 上为1，由 \(F^*F=M_\nu\) 得 \(F=FM_\chi\)。对 \(B\in G_M\)，
\[
 FBF^*=FM_\chi B M_\chi F^*\in\mathcal S_1,                \tag{14}
\]
因为 \(M_\chi B M_\chi\) 具有光滑紧支二维核。不能把(14)外推到任意有界B；紧支时间乘法不自动紧或迹类。例如B=1时 \(FF^*\) 一般非紧，只要ν在某区间严格正，就能用该区间中的高频弱零向量证明。平滑性准入仍是必要的证明条件。

## 7. 附加可审范数公式：允许端质量有零点

对任意 \(B\in G_M\)，还可精算
\[
 \boxed{\|FBF^*\|_{\rm ess}=\|M_{\sqrt w}B M_{\sqrt w}\|.} \tag{15}
\]
这里不要求w有严格正下界；\(\sqrt w\) 未必光滑，但有界周期即可。证明上界：取F的极分解 \(F=J_0M_{\sqrt\nu}\)。\(T_\nu=M_{\sqrt\nu}BM_{\sqrt\nu}\) 两侧输入左支集固定；取充分右半线P，使ν=w。\(T_\nu-PT_\nu P\) 的两项都有一侧变量被限于有限区间，B有限传播把另一变量也限于紧区间。先用光滑χ的紧支二维核支付迹类，再乘 \(\sqrt\nu\) 和sharp示性函数等有界因子，故差为迹类。于是
\[
 FBF^*=J_0P(M_{\sqrt w}BM_{\sqrt w})PJ_0^*+\mathcal S_1,
 \qquad\|FBF^*\|_{\rm ess}\le\|M_{\sqrt w}BM_{\sqrt w}\|.
\]

下界：右侧H消灭w=0集合，范数可由 \(C_c^\infty(\{w>0\})\) 的单位向量ψ逼近，因为该类稠密于 \(\mathbf1_{\{w>0\}}L^2\)。对固定这样的ψ，支集内 \(w\ge\epsilon>0\)。以nM右移，\(\eta_n=FM_{w^{-1/2}}\psi_n\) 是单位弱零列；倒平方根仅用于这个严格正的紧支上。有限传播保证输出也在ν=w端，准确有
\[
 \|FBF^*\eta_n\|
 =\|M_{\sqrt w}BM_{\sqrt w}\psi_n\|
 =\|H\psi\|.
\]
取紧扰动和上述向量的上确界支付下界。w恒零时右侧为0，与(14)的更强迹类结论相容。(15)范围仅为明确G_M核，不给任意有界B作未经证明的端范数公式。

## 8. 原最小源理想中的固定点及读出范围

令旧E为428的原范数完成，\(\mathcal C=C^*(1,u,E)\)，\(\mathcal J\) 为E在C中生成的最小闭理想。对(10)的 \(B=U(h)\)，种子 \(VBV^*=A(h)\in E\)。每个 \(u^jA(h)u^{-j}\) 在J内，J范数闭，故X由(6)真实属于原最小J；此论证不依赖把解析扩大域认作最小理想。w非零时X非紧，于是其在 \(\mathcal J/\mathcal K\) 中给非零源共轭固定符号。

这个平均由真实u和指定种子决定，但不产生物理 \(\Lambda\) 的唯一规范读出。普通迹或原有限部未被证明沿(6)连续：迹在算子范数中不连续，而428已证明原周期分布也不连续于旧符号一致范数。因此不能把有限平均的周期值直接传给X；本文没有循环链、相对Chern配对或主关系消失的新结论。

结论是一个真实的完成域固定部门，以及严格的有限词／范数完成区别。原球截止比较、实位与全素数Weil读出、RR、Weil正性和RH均保持开放。
