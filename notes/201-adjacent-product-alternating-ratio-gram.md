# 201. 相邻乘积 Gram、交替比值 Gram 与窗口边缘抑制

日期：2026-09-01

状态：有限 Gabor 的 2+2 非交换 Gram 分解、乘积/比值聚类、换位子恒等式
与 bulk path-support lemma 为 [T]；adjacent edge tightness 和 alternating
response-specific Farey bound 为 [O]。

## 1. 本轮最重要的缩减

纯素数四矩的六个 \(2+2\) 循环词不是同一种算术对象：

- 四个 adjacent words 按乘积 \(m=ab\) 聚类；理想 compact-support bulk
  强制 \(ab\le X\)，所以只具有长度 \(X\)；
- 两个 alternating words 按既约比值 \(\rho=a/b\) 聚类；Farey 间距可小到
  \(X^{-2}\)，这是普通 large sieve 不闭合的真正硬通道。

因此旧目标“统一估计全部 \(n_1n_2\approx n_3n_4\)”可以严格缩成：

1. 用边缘 tightness 加 vector-valued Montgomery--Vaughan 处理 adjacent
   product Gram；
2. 只对 alternating ratio Gram 建立 response-specific Vaughan--Schur 证书。

## 2. 真实有限 Gabor 矩阵的精确分解 [T]

令

\[
 \mathbf f(\tau)=(f_0(\tau),\ldots,f_{d-1}(\tau))^{\mathsf T},
 \qquad c_T=\frac1{aL^2},
\]

\[
 R_T(x)=c_T\int_{\mathbb R}
 \mathbf f(\tau)\mathbf f(\tau)^*e^{ix\tau}\,d\tau.
\tag{1}
\]

则 \(R_T(-x)=R_T(x)^*\)。取

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},qquad
 Z_T=\sum_{n\le X}b_nR_T(\log n).
\tag{2}
\]

有限压缩的纯素数矩阵为

\[
 P_T=Z_T+Z_T^*.
\]

### 定理 AEK（two-family Gram factorization）

从 \(\operatorname{tr}P_T^4\) 中抽取恰有两个 \(Z_T\) 与两个
\(Z_T^*\) 的六个词，则

\[
 \boxed{
 [\operatorname{tr}P_T^4]_{2+2}
 =4\|Z_T^2\|_{\rm HS}^2
 +2\|Z_TZ_T^*\|_{\rm HS}^2.}
\tag{3}
\]

四个 adjacent words 是
\(\operatorname{tr}(Z^2(Z^*)^2)=\|Z^2\|_{\rm HS}^2\) 的循环旋转；
两个 alternating words 是
\(\operatorname{tr}(ZZ^*ZZ^*)=\|ZZ^*\|_{\rm HS}^2\)。

两个完整 family 都是 PSD Gram；但从完整 Gram 删除 block diagonal 后的
off-diagonal 一般没有固定符号。

## 3. 非交换换位子预算 [T]

令

\[
 A=\|Z^2\|_{\rm HS}^2,qquad
 B=\|ZZ^*\|_{\rm HS}^2,qquad
 C=\|[Z,Z^*]\|_{\rm HS}^2.
\]

直接展开给

\[
 C=2(B-A),qquad 0\le A\le B.
\tag{4}
\]

所以式 (3) 还可写成

\[
 [\operatorname{tr}P_T^4]_{2+2}
 =6A+C=6B-2C.
\tag{5}
\]

这给出一个新的结构解释：alternating 与 adjacent 的差不是偶然的窗口常数，
而是正的 non-normality/commutator energy。对平窗的配对对角，单个 adjacent
与 alternating word 分别为 \(1/60\) 与 \(1/10\)，故对角换位子能量为
\(1/6\)。

完整素数词账本为

\[
 \operatorname{tr}(Z+Z^*)^4
 =2\operatorname{Re}\operatorname{tr}Z^4
 +8\operatorname{Re}\operatorname{tr}(Z^3Z^*)
 +4A+2B.
\tag{6}
\]

## 4. adjacent 按乘积聚类 [T]

记 \(R_n=R_T(\log n)\)，定义

\[
 F_m^{\rm adj}
 =\sum_{\substack{a,b\le X\\ab=m}}
 b_ab_bR_aR_b.
\tag{7}
\]

则

\[
 Z_T^2=\sum_mF_m^{\rm adj},qquad
 \|Z_T^2\|_{\rm HS}^2
 =\sum_{m,n}\Gamma^{\rm adj}_{m,n},
\tag{8}
\]

其中

\[
 \Gamma^{\rm adj}_{m,n}
 =\langle F_m^{\rm adj},F_n^{\rm adj}\rangle_{\rm HS}
\tag{9}
\]

即

\[
 \Gamma^{\rm adj}_{m,n}
 =\sum_{\substack{ab=m\\cd=n}}
 \overline{b_ab_b}\,b_cb_d
 \operatorname{tr}(R_b^*R_a^*R_cR_d).
\tag{10}
\]

故 \(\Gamma^{\rm adj}\succeq0\)。

## 5. alternating 按既约比值聚类 [T]

令 \(\rho=p/q>0\) 为既约正有理数，定义

\[
 F_\rho^{\rm alt}
 =\sum_{\substack{a,b\le X\\a/b=\rho}}
 b_a\overline{b_b}R_aR_b^*
 =\sum_k b_{kp}\overline{b_{kq}}R_{kp}R_{kq}^*.
\tag{11}
\]

则

\[
 Z_TZ_T^*=\sum_\rho F_\rho^{\rm alt},
\qquad
 \|Z_TZ_T^*\|_{\rm HS}^2
 =\sum_{\rho,\sigma}\Gamma^{\rm alt}_{\rho,\sigma},
\tag{12}
\]

\[
 \Gamma^{\rm alt}_{\rho,\sigma}
 =\langle F_\rho^{\rm alt},F_\sigma^{\rm alt}\rangle_{\rm HS}
 \succeq0.
\tag{13}
\]

展开后

\[
 \Gamma^{\rm alt}_{\rho,\sigma}
 =\sum_{\substack{a/b=\rho\\c/d=\sigma}}
 \overline{b_a}b_b b_c\overline{b_d}
 \operatorname{tr}(R_bR_a^*R_cR_d^*).
\tag{14}
\]

近对角条件

\[
 \log\rho\approx\log\sigma
 \quad\Longleftrightarrow\quad ad\approx bc
\]

经重命名就是 \(n_1n_2\approx n_3n_4\)。完整 \(2+2\) 账本为

\[
 E_{22}=4\mathbf1^*\Gamma^{\rm adj}\mathbf1
 +2\mathbf1^*\Gamma^{\rm alt}\mathbf1.
\tag{15}
\]

虽然两张 \(\Gamma\) 均 PSD，
\(\Gamma-\operatorname{diag}\Gamma\) 通常不 PSD：任一非零的
\(2\times2\) 交叉块 \(z\) 在删去对角后已有特征值 \(\pm|z|\)。

## 6. translation-invariant bulk 的 path kernel [T]

令

\[
 \Phi_L(x)=\int q_L(u)e^{-iux}du,qquad
 q_L(u)=\psi(u/L),
\]

并以 \(w_T\) 表示共同时间 cutoff。若
\(\Omega=\lambda_1+\cdots+\lambda_4\)，则 one-cut
translation-invariant bulk 精确满足

\[
 \begin{aligned}
 &\int_{\mathbb R^4}w_T(\tau_4)
 \prod_{j=1}^4\Phi_L(\tau_j-\tau_{j+1})
 e^{i\sum_j\lambda_j\tau_j}\,d\tau_1\cdots d\tau_4\\
 &\qquad=(2\pi)^3\widehat w_T(\Omega)L
 \mathcal W_\psi(s_0,s_1,s_2,s_3),
 \end{aligned}
\tag{16}
\]

其中 \(\tau_5=\tau_1\)，

\[
 s_0=0,\quad s_1=\frac{\lambda_1}{L},\quad
 s_2=\frac{\lambda_1+\lambda_2}{L},\quad
 s_3=\frac{\lambda_1+\lambda_2+\lambda_3}{L},
\]

\[
 \mathcal W_\psi(s_0,s_1,s_2,s_3)
 =\int_{\mathbb R}\prod_{j=0}^3\psi(u+s_j)du.
\tag{17}
\]

所以公共频率核 \(\widehat w_T(\Omega)\) 读取总乘法失配，非负 path overlap
读取循环词的部分和路径。真实 \(I^4\) 截断不等于 one-cut 模型；两者差异正是
笔记 200 的 finite-to-bulk gate。

## 7. adjacent 实际只有长度 \(X\) [T]

置 \(r_n=\log n/L\in[0,1]\)。对 adjacent 次序 \(+,+,-,-\)，部分和
包含

\[
 0,\quad r_a,\quad r_a+r_b.
\]

因为 \(\psi\) 支撑于长度为 \(1\) 的区间，式 (17) 非零要求

\[
 \max_js_j-\min_js_j\le1.
\tag{18}
\]

故

\[
 r_a+r_b\le1,qquad\boxed{ab\le X}.
\tag{19}
\]

相邻通道不同乘积频率的间距为 \(\gg X^{-1}\)，在 \(T\asymp X\) 上处于
普通 vector-valued Montgomery--Vaughan 的临界长度，而不是长度 \(X^2\)。

对 alternating 次序 \(+,-,+,-\)，部分和为

\[
 0,\quad r_a,\quad r_a-r_b,\quad r_a-r_b+r_c.
\]

式 (18) 不推出正频乘积小于 \(X\)。既约比值的分母仍可达 \(X\)，Farey
间距约 \(X^{-2}\)；普通 large sieve 给 \(T+X^2\)，不能闭合。

## 8. 窗口对边缘 path 的作用 [T]

令

\[
 R=\max_js_j-\min_js_j,qquad \ell=1-R.
\]

平窗精确给 \(\mathcal W_{\rm flat}=\ell_+\)。对

\[
 \psi_c(u)=\cos(cu)\mathbf1_{|u|\le1/2},qquad0<c\le\pi,
\]

记 \(v_c=\cos(c/2)\)，则

\[
 0\le\mathcal W_c(s)
 \le v_c^2\ell+v_cc\ell^2+\frac{c^2}{6}\ell^3.
\tag{20}
\]

证明是在交集区间写 \(u=-1/2+x\)、\(0\le x\le\ell\)。达到最小和最大
shift 的两个因子分别不超过
\(v_c+cx\)、\(v_c+c(\ell-x)\)，另两因子不超过 \(1\)，再积分。

因此 MT 窗仍只有 \(O(\ell)\)，但端点窗满足

\[
 \boxed{\mathcal W_\pi(s)\le\frac{\pi^2}{6}\ell^3.}
\tag{21}
\]

若极值 shift 唯一，另两个极限 shift 为
\(s_2,s_3\in(0,1)\)，则

\[
 \mathcal W_\pi(s)
 =\frac{\pi^2}{6}\sin(\pi s_2)\sin(\pi s_3)\ell^3
 +O(\ell^4).
\tag{22}
\]

这解释了 \(c\uparrow\pi\) 对最难边缘 path 的强抑制。但它不是逐点优势：
所有 shifts 重合时，归一化中心 overlap 为

\[
 \frac{\int_{-1/2}^{1/2}\cos^4(\pi u)du}{(2/\pi)^4}
 =\frac{3\pi^4}{128}>1,
\tag{23}
\]

反而大于平窗。故 \(D_{22}\) 变小不能自动推出未配对 remainder 变小。

## 9. 最小一侧估计 [C/O]

最弱并保留符号的条件是

\[
 \frac4N\mathbf1^*(\Gamma^{\rm adj}-D^{\rm adj})\mathbf1
 +\frac2N\mathbf1^*(\Gamma^{\rm alt}-D^{\rm alt})\mathbf1
 \le\eta_{22}+o(1).
\tag{24}
\]

一个更强的 family-wise frame 条件为

\[
 \left\|\sum_mF_m^{\rm adj}\right\|_{\rm HS}^2
 \le(1+\varepsilon_{\rm adj})
 \sum_m\|F_m^{\rm adj}\|_{\rm HS}^2+o(N),
\tag{25}
\]

\[
 \left\|\sum_\rho F_\rho^{\rm alt}\right\|_{\rm HS}^2
 \le(1+\varepsilon_{\rm alt})
 \sum_\rho\|F_\rho^{\rm alt}\|_{\rm HS}^2+o(N).
\tag{26}
\]

对 MT 窗，额外 \(2+2\) 预算为

\[
 0.0664321521\,\varepsilon_{\rm adj}
 +0.1781572299\,\varepsilon_{\rm alt}.
\tag{27}
\]

它与 \(3+1,4+0\)、背景及 finite-to-bulk 余项之和必须小于
\(0.0829099143\)。端点余弦窗的相应权重为

\[
 0.0563628586\,\varepsilon_{\rm adj}
 +0.1091501834\,\varepsilon_{\rm alt},
\]

总余项预算约 \(0.1982670070\)。

## 10. adjacent 的下一条可证 lemma [C/O]

固定 \(\delta>0\)。在 \(m\le X^{1-\delta}\) 上，vector-valued large
sieve 给相对误差 \(O(X^{1-\delta}/T)=O(T^{-\delta})\)。因此只要证明

\[
 \lim_{\delta\downarrow0}\limsup_{T\to\infty}
 \frac1N\sum_{X^{1-\delta}<m\le X}
 \|F_m^{\rm adj}\|_{\rm HS}^2=0,
\tag{28}
\]

并建立与真实 Gabor 边界相容的 vector-valued disintegration，式 (25) 可取
\(\varepsilon_{\rm adj}=0\)。平窗的 \(O(\ell)\) 已使候选对角 edge mass
紧，端点窗的 \(O(\ell^3)\) 提供更强裕量；正式证明仍需完成。

## 11. alternating 的 response-specific Schur 终点 [C/O]

普通 all-direction large sieve 过强。令 \(\mathcal R_{\rm alt}\) 把有限
Type I/II/Vaughan channel 坐标映到细比值空间，并置

\[
 G=\mathcal R_{\rm alt}^*\Gamma^{\rm alt}\mathcal R_{\rm alt},
 \qquad
 D=\mathcal R_{\rm alt}^*D^{\rm alt}\mathcal R_{\rm alt}.
\]

一个可审计证书是寻找 \(M\succeq0\) 使

\[
 Q=(1+\varepsilon_{\rm alt})D+M-G\succeq0,
\tag{29}
\]

且对真实 channel vector \(x\)，\(x^*Mx\le\eta_{\rm alt}N\)。分成
easy/hard 后，式 (29) 等价于标准 Schur 条件

\[
 Q_{ee}\succeq0,qquad
 \operatorname{ran}Q_{eh}\subseteq\operatorname{ran}Q_{ee},
\]

\[
 Q_{hh}-Q_{he}Q_{ee}^{\dagger}Q_{eh}\succeq0.
\tag{30}
\]

这只在真实 Vaughan response 子空间上控制 alternating Farey Gram，不要求
对任意比值系数成立。

若需按近共振尺度局部化，不应使用硬 band mask，因为它通常不 PSD。应使用
triangular/Fej\'er 正定 mask，或

\[
 M_{\mu\nu}=\sum_j\chi_j(\log\mu)\overline{\chi_j(\log\nu)},
\]

再以 Schur product 保持 PSD。

审计脚本 scripts/operator_fourth_localizer_audit.py 验证式 (3)--(15) 的有限矩阵
恒等式与乘积/比值聚类，并数值审计式 (20)--(23)。它不证明式 (28)--(30)。

