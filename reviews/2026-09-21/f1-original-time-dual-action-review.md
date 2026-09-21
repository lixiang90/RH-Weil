# 原时间对偶作用独立复核

2026-09-21。完整原始回报见 [raw](f1-original-time-dual-action-review.raw.json)。

**核验通过：未发现对偶相位、深边界旋转或频率阈值的符号错误。** 以下给出逐项核对及与已完成 Hardy 指数族的衔接。只读检查了[计算稿](H:/codex-build/RH/RH-Weil/reviews/2026-09-21/f1-original-time-dual-action-calculation.md)，未修改文件。

1. **对偶作用与 \(\Phi\) 下的分解一致。**

按稿件明确采用的约定，
\[
\widehat\beta_\nu|_{i_A(A)}=\mathrm{id},\qquad
\widehat\beta_\nu(V_s)=e^{i\nu s}V_s.
\]
这里“固定原 \(A\)”是对其规范乘子像逐元素固定。因此
\[
\widehat\beta_\nu(P_g)=P_g,\qquad
\boxed{\widehat\beta_\nu(Z_g)=e^{-i\nu\ell_g}Z_g.}
\tag{1}
\]

另一方面，
\[
M_\nu T_sM_\nu^*=e^{i\nu s}T_s.
\]
结合
\[
\Phi(P_g)=z_g\otimes T_{\ell_g},\quad
\Phi(V_s)=1\otimes T_s,\quad
\Phi(Z_g)=z_g\otimes1,
\]
得到
\[
\boxed{
\Phi\widehat\beta_\nu\Phi^{-1}
=\gamma_\nu\otimes\operatorname{Ad}M_\nu,
\qquad
\gamma_\nu(z_g)=e^{-i\nu\ell_g}z_g.
}
\tag{2}
\]
特别地，\(P_g\) 上两因子相位相反，准确抵消。

深边界的公式因而是
\[
\boxed{
(\widehat\beta_\nu F)(\zeta)
=M_\nu F(r_\nu\zeta)M_\nu^*,
}
\tag{3}
\]
其中
\[
r_\nu(\zeta_p,\zeta_q)
=(e^{-i\nu L}\zeta_p,e^{-i\nu M}\zeta_q).
\]
对坐标函数 \(\zeta^g\) 代入即可检查负号。

稿件的连续性表述也正确：\(\gamma_\nu\) 和
\(\operatorname{Ad}M_\nu|_{\mathbb K_t}\) 逐元素范数连续；不需要、也不能据此声称 \(M_\nu\) 本身算子范数连续。

2. **原表示的实施酉及截止变换正确。**

令
\[
R_\nu=D_\nu\otimes M_\nu,\qquad
D_\nu\delta_m=e^{-i\nu\ell_m}\delta_m.
\]
直接计算
\[
D_\nu\lambda_gD_\nu^*=e^{-i\nu\ell_g}\lambda_g.
\]
故原表示中
\[
R_\nu(\lambda_g\otimes T_{\ell_g})R_\nu^*
=\lambda_g\otimes T_{\ell_g}.
\]
原系数乘法算子也与 \(R_\nu\) 交换，而
\[
R_\nu(1\otimes T_s)R_\nu^*
=e^{i\nu s}(1\otimes T_s).
\]
因此
\[
\boxed{
\Pi(\widehat\beta_\nu(b))
=R_\nu\Pi(b)R_\nu^*.
}
\tag{4}
\]

在原坐标上，\(R_\nu\) 是乘法
\[
e^{i\nu(t-\ell_m)};
\]
在 \(x=t-\ell_m\) 坐标上就是 \(e^{i\nu x}\)。这核准了它与原 \(\pi(A)\) 交换的说法。

这里的实施酉位于具体表示的 \(B(\mathcal H)\)；不能仅由 (4) 宣称对偶作用是交叉积乘子内部的内自同构。

因为 \(M_\nu\) 与 \(M_{d_\alpha}\) 交换，
\[
\boxed{
C_N^\nu=R_\nu C_NR_\nu^*
=\sum_\alpha D_\nu E_\alpha D_\nu^*
 \otimes M_{d_\alpha}.
}
\tag{5}
\]
各 \(E_\alpha\) 有限秩，所以其共轭仍属于径向紧算子理想；(5) 与将 \(C_N\) 放在时间交叉积乘子代数中的解释相容。原截止一般不固定。

3. **完整 \(\Gamma\) 迹的相位确实逐项抵消。**

定义
\[
h_\nu(s)=e^{i\nu s}h(s).
\]
由于原 \(P_g\) 固定，
\[
\boxed{
R_\nu\bigl(C_NP_gU(h)C_N\bigr)R_\nu^*
=C_N^\nu P_gU(h_\nu)C_N^\nu.
}
\tag{6}
\]
因此每项的迹范数保持不变，原绝对迹范数收敛立即传递到右侧，并有
\[
R_\nu A_N(h)R_\nu^*
=\sum_gC_N^\nu P_gU(h_\nu)C_N^\nu.
\tag{7}
\]
这无需重新从调制后的导数界证明收敛。

直接求迹也核准稿件中的符号。径向对角块满足
\[
\operatorname{Tr}
\bigl(E_\alpha^\nu\lambda_gE_\alpha^\nu\bigr)
=e^{i\nu\ell_g}
\operatorname{Tr}(E_\alpha\lambda_gE_\alpha),
\tag{8}
\]
而时间对角因子为
\[
h_\nu(-\ell_g)
=e^{-i\nu\ell_g}h(-\ell_g).
\tag{9}
\]
两相位相消。交叉块仍因
\[
E_\alpha^\nu E_\beta^\nu=0\quad(\alpha\ne\beta)
\]
而具有零横向迹。因此对全部 \(g\) 都成立，没有预先删除混合次数。

结论是
\[
\boxed{
\operatorname{Tr}\bigl(R_\nu A_N(h)R_\nu^*\bigr)
=\operatorname{Tr}A_N(h),
}
\tag{10}
\]
**不是**
\(\operatorname{Tr}A_N(h_\nu)=\operatorname{Tr}A_N(h)\)。

若整合稿尚未给出 \(A_N(h)\) 属于时间交叉积的证明，(7)–(10) 可先作为 \(B(\mathcal H)\) 中的实施酉恒等式使用；援引 419 的归属结论后，再直接写成
\(\widehat\beta_\nu(A_N(h))\)。这是证明依赖，并非公式错误。

4. **实际源固定与阈值压缩的等变式正确。**

源族中的每个非恒等单项形如
\[
\zeta_p^n\zeta_q^bM_fT_{nL+bM}.
\]
代入 \(r_\nu\zeta\) 产生相位
\(e^{-i\nu(nL+bM)}\)，而 \(\operatorname{Ad}M_\nu\) 产生相反相位。故逐项有
\[
\boxed{M_\nu u_{r_\nu\zeta}M_\nu^*=u_\zeta.}
\tag{11}
\]
这里“源固定”指**整个乘子截面在基空间旋转和时间共轭的联合作用下固定**；并非单独断言 \(u_{r_\nu\zeta}=u_\zeta\)。

给定 Fourier 约定下，
\[
\widehat{M_\nu f}(\xi)=\widehat f(\xi-\nu),
\]
因此
\[
\boxed{
M_\nu P_+M_\nu^*=P_\nu
=\mathbf1_{[\nu,\infty)}(\xi).
}
\tag{12}
\]
结合 (11)，得到稿件中的准确等变式
\[
\boxed{
P_\nu u_\zeta P_\nu
=M_\nu\bigl(P_+u_{r_\nu\zeta}P_+\bigr)M_\nu^*.
}
\tag{13}
\]

应明确其 Fredholm 解释：左侧作用在
\[
\mathcal H_\nu=P_\nu L^2(\mathbb R),
\]
而 \(M_\nu:\mathcal H_+\to\mathcal H_\nu\) 是酉同构。故已有真实 Hardy Fredholm 族立即给出所有阈值的 Fredholm 族，不需要任何紧扰动论证。

5. **投影差不紧，但指数传递不受影响。**

对 \(\nu\ne0\)，
\[
P_\nu-P_+
=
\begin{cases}
-\mathbf1_{[0,\nu)}(\xi),&\nu>0,\\
+\mathbf1_{[\nu,0)}(\xi),&\nu<0.
\end{cases}
\tag{14}
\]
非零有限区间上的 \(L^2\) 空间仍为无限维，故该投影差无限秩、不紧，范数为 \(1\)。更一般，
\[
\|P_\nu-P_\mu\|=1\qquad(\nu\ne\mu).
\]
因此不能把这些投影视为固定 Hilbert 空间上的范数连续投影路径。

但用 \(M_\nu\) 识别移动的 Hilbert 空间后，(13) 变成
\[
M_\nu^*
\bigl(P_\nu u_\zeta P_\nu|_{\mathcal H_\nu}\bigr)M_\nu
=T_0(r_\nu\zeta).
\tag{15}
\]
右侧是已证范数连续的参数族。因此这一识别后，连 \((\nu,\zeta)\) 的联合范数连续性也直接成立。

指数束满足
\[
\boxed{\operatorname{Ind}T_\nu=r_\nu^*\operatorname{Ind}T_0.}
\tag{16}
\]
\(r_\nu\) 是与恒等同伦的环面平移，所以普通 \(K^0\) 类不变。接上已经完成的实际指数计算，每个阈值仍有
\[
\operatorname{rank}\operatorname{Ind}T_\nu=0,\qquad
\langle c_1(\operatorname{Ind}T_\nu),[\mathbb T^2]\rangle=-1,
\]
沿用 \((\arg\zeta_p,\arg\zeta_q)\) 的定向和“核减余核”约定。

稿件最后的信息边界判断正确：**带标记的对偶作用保留**
\[
\ell_g=g_1L+g_2M
\]
及频率 \(L,M\)；普通指数类本身则只有这里的秩与 Chern 数据，且所有 \(r_\nu\) 在普通 \(K^0\) 上作用相同。它不能据此恢复完整周期迹。后续应同时保存对偶作用、原截止及测试算子的变换规则，不能用普通指数类替代这些数据。
