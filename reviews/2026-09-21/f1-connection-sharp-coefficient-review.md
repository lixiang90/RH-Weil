# 418：近锐分割p系数的独立核验

2026-09-21。原始回包见[raw](f1-connection-sharp-coefficient-review.raw.json)。仅添加标题和本段，将本地路径改为相对链接。报告给出比主稿更强的界；主稿保留较宽但足够的界。

**成立，且候选界可以加强。** 对题设
\[
m_S=4+2\lceil S/L\rceil
\]
有
\[
\boxed{
\sup_{|s|\le S}|J_{p,\varepsilon}(s)-L|
\le
\frac{\varepsilon}{2}\sqrt{2m_S}
+2\varepsilon(\sqrt2-1).
}
\tag{1}
\]
因此题设较宽的界也成立。特别地，\(J_{p,\varepsilon}\to L\) 在每个紧时间区间一致成立，足以排除所述“对所有合法分割成立的直接补偿”。

以下只核验这一侧题。已只读核对 [417](../../notes/417-f1-projection-connection-and-time-evolution.md) 的定义，未修改文件。

1. **纤维表示、指标与时间符号。**

对 \(t\in[0,L)\)，采用轨道表示
\[
(\pi_t(fU_p^n)\xi)(j)
=f(t+jL)\xi(j-n).
\tag{2}
\]
它与原协变约定 \(U_pf(t)U_p^*=f(t-L)\) 一致。令
\[
c_t(j)=c_\varepsilon(t+jL).
\]
则
\[
\|c_t\|_2^2=1,\qquad
\pi_t(e)=c_tc_t^T,\qquad
\pi_t(K)=c'_tc_t^T-c_t(c'_t)^T.
\tag{3}
\]

因为 \(\beta_{-s}\) 将系数变为 \(f(\,\cdot+s)\)，实际纤维演化满足
\[
\partial_sW_s(t)=K(t+s)W_s(t),\qquad W_0(t)=1.
\tag{4}
\]
这里确实是 \(t+s\)，不是 \(t-s\)。

由平方分割求导，
\[
(c'_{t+s})^Tc_{t+s}=0,
\]
所以
\[
K(t+s)c_{t+s}=c'_{t+s}.
\]
因此 \(W_s(t)c_t\) 与 \(c_{t+s}\) 解同一个初值问题，得到
\[
\boxed{W_s(t)c_t=c_{t+s}.}
\tag{5}
\]
正负 \(s\) 均成立。

式中 \(c_{t+s}(j)=c_\varepsilon(t+s+jL)\) 按实数参数直接解释；若把 \(t+s\) 重新取模 \(L\)，必须同时重标坐标。具体地，若
\[
(\mathsf S\xi)(j)=\xi(j-1),
\]
则
\[
c_{t+L}=\mathsf S^{-1}c_t,\qquad
W_s(t+L)=\mathsf S^{-1}W_s(t)\mathsf S.
\]
这也核准了基本区间端点的相容性。

2. **输出有限支撑及统一坐标数。**

令
\[
J=\operatorname{supp}c_\varepsilon
\subset[-\varepsilon,L+\varepsilon].
\]
由于 \(\operatorname{supp}c'_\varepsilon\subset J\)，矩阵
\(K(t+r)\) 的非零行、非零列都满足
\[
t+jL+r\in J.
\]
固定 \(t,S\)，取有限集合
\[
E_{t,S}
=\{j\in\mathbb Z:
t+jL\in[-\varepsilon-S,L+\varepsilon+S]\}.
\tag{6}
\]
若 \(P_{t,S}\) 是相应坐标投影，则对全部 \(|r|\le S\)，
\[
K(t+r)=P_{t,S}K(t+r)P_{t,S}.
\]
由演化方程唯一性，
\[
W_s(t)
=
W_s(t)|_{\ell^2(E_{t,S})}
\oplus 1_{\ell^2(E_{t,S}^c)},
\qquad |s|\le S.
\tag{7}
\]
有限块中的生成矩阵实反对称，故 \(W_s(t)\) 保持 \(\ell^2\) 范数。

区间 (6) 的长度为 \(L+2\varepsilon+2S\)，所以
\[
\begin{aligned}
\#E_{t,S}
&\le
\left\lfloor1+\frac{2\varepsilon}{L}
+\frac{2S}{L}\right\rfloor+1\\
&\le 2+2\lceil S/L\rceil
\le m_S.
\end{aligned}
\tag{8}
\]
这里使用 \(2\varepsilon/L<1/2\)。因此题设的 \(m_S\) 是安全上界。

尤其令
\[
z_t=c_t^{\odot2}-c_t.
\]
其初始支撑已经包含于 \(E_{t,S}\)，故由 (7)
\[
\operatorname{supp}(W_s(t)z_t)\subset E_{t,S}.
\tag{9}
\]
这一步覆盖了演化中的恒等部分；仅知道 \(W_s-1\) 输出有限支撑还不够，必须同时检查 \(z_t\) 的初始支撑。

因此可以合法定义有限坐标求和，并有
\[
\left|\sum_j(W_s(t)z_t)(j)\right|
\le\sqrt{m_S}\,\|W_s(t)z_t\|_2
=\sqrt{m_S}\,\|z_t\|_2.
\tag{10}
\]
这里没有把 \(\mathbf1\) 当成 \(\ell^2\) 向量。

此外，对全部 \(t\in[0,L)\)，上述支撑还包含于一个共同有限整数集合，例如令 \(m=\lceil S/L\rceil\)，可取
\[
\{-m-1,\ldots,m+1\}.
\]
因此以下积分中的坐标求和也不存在无限交换问题。

3. **\(J_p(s)\) 的纤维公式准确，无额外归一化因子。**

沿用已经建立的系数记号
\[
W_s=\sum_n M_{w_n(s,\cdot)}P_{(n,0)}.
\]
由 (2)，纤维矩阵元为
\[
(W_s(t))_{jk}
=w_{j-k}(s,t+jL).
\tag{11}
\]
原周期化计算中的系数定义是
\[
J_p(s)=
\int_{\mathbb R}c_\varepsilon(x)^2
\sum_n w_n(s,x+nL)\,dx.
\tag{12}
\]
令 \(x=t+kL\)，再令 \(j=k+n\)，得到
\[
\begin{aligned}
J_p(s)
&=\int_0^L\sum_k c_\varepsilon(t+kL)^2
 \sum_j w_{j-k}(s,t+jL)\,dt\\
&=\boxed{
\int_0^L\sum_j
\bigl(W_s(t)c_t^{\odot2}\bigr)(j)\,dt.
}
\end{aligned}
\tag{13}
\]
因此题设的
\(\int_0^L\mathbf1^TW_s(t)c_t^{\odot2}\,dt\)
正确，只需按有限输出坐标求和解释。

此处使用普通 Lebesgue 测度 \(dt\)，不是 \(dt/L\)。将实轴拆成
\([kL,(k+1)L)\) 不产生额外 \(L\) 或 \(1/L\) 因子。

4. **坏集的模 \(L\) 测度为 \(2\varepsilon\)。**

对于 417 的分割，在
\[
t\in[\varepsilon,L-\varepsilon]
\]
上，\(c_t\) 恰为第 \(0\) 个标准基向量。因此
\[
z_t=0
\quad\text{在}\quad
[0,L)\setminus T_\varepsilon,
\]
其中可取
\[
T_\varepsilon=[0,\varepsilon)\cup[L-\varepsilon,L),
\qquad |T_\varepsilon|=2\varepsilon.
\tag{14}
\]
两段实轴过渡区模 \(L\) 后重合为一个长度 \(2\varepsilon\) 的过渡区；这里不能重复计成 \(4\varepsilon\)。

具体指标也一致：

- \(t\in[0,\varepsilon)\) 时，可能非零的是坐标 \(0,1\)，值为
  \(\sin\theta(t),\cos\theta(t)\)；
- \(t\in[L-\varepsilon,L)\) 时，令 \(r=t-L\)，可能非零的是坐标 \(-1,0\)，值为
  \(\sin\theta(r),\cos\theta(r)\)。

每个 \(c_t\) 至多两个非零坐标，且各坐标属于 \([0,1]\)。由
\[
|x^2-x|\le\frac14\qquad(0\le x\le1)
\]
可得
\[
\boxed{\|z_t\|_2\le\frac{\sqrt2}{4}.}
\tag{15}
\]
所以题设较粗的 \(\sqrt2\) 界当然成立，而所提示的
\(\sqrt2/4\) 界也确实有效。

5. **积分主项与误差估计。**

由 (5)、(13)，
\[
\begin{aligned}
J_p(s)
&=\int_0^L\sum_j c_\varepsilon(t+s+jL)\,dt
 +E_\varepsilon(s),\\
E_\varepsilon(s)
&=\int_0^L\sum_j(W_s(t)z_t)(j)\,dt.
\end{aligned}
\tag{16}
\]
第一项准确等于
\[
\boxed{
\int_0^L\sum_j c_\varepsilon(t+s+jL)\,dt
=\int_{\mathbb R}c_\varepsilon(x)\,dx.
}
\tag{17}
\]
理由是区间 \([s+jL,s+(j+1)L)\) 随 \(j\) 分割实轴；这对负 \(s\) 同样成立。

另一方面，\(\sum_jc_\varepsilon(t+jL)^2=1\)、非负性及至多两个非零坐标给
\[
1\le\sum_jc_\varepsilon(t+jL)\le\sqrt2.
\]
在 \(T_\varepsilon\) 外，该和准确为 \(1\)。故
\[
\boxed{
0\le\int_{\mathbb R}c_\varepsilon(x)\,dx-L
\le2\varepsilon(\sqrt2-1).
}
\tag{18}
\]
也可直接写成
\[
\int c_\varepsilon-L
=\int_{-\varepsilon}^{\varepsilon}
\bigl(\sin\theta(r)+\cos\theta(r)-1\bigr)\,dr.
\]
没有遗漏两个过渡段中的任何一段。

由 (10)、(14)、(15)，对全部 \(|s|\le S\)，
\[
\begin{aligned}
|E_\varepsilon(s)|
&\le\int_{T_\varepsilon}
\sqrt{m_S}\,\|z_t\|_2\,dt\\
&\le
2\varepsilon\sqrt{m_S}\,\frac{\sqrt2}{4}
=\frac{\varepsilon}{2}\sqrt{2m_S}.
\end{aligned}
\tag{19}
\]
结合 (16)–(19)，得到开头的 (1)，并特别推出题设所问的界
\[
|J_p(s)-L|
\le2\varepsilon\sqrt{2m_S}
 +2\varepsilon(\sqrt2-1).
\]

证明只使用酉性、有限输出支撑和过渡区测度，**不需要**
\(K_\varepsilon\) 或其导数在 \(\varepsilon\to0\) 时一致有界。

6. **对直接边界补偿的限制。**

固定任意 \(a\ne0\)，取 \(S\ge|a|L\)，由 (1)
\[
\boxed{J_{p,\varepsilon}(-aL)-L\longrightarrow0.}
\tag{20}
\]

用 414 的 \(1/2\) 归一化，记
\[
\Delta_\varepsilon(h)
=\frac12\operatorname{Tr}
 \bigl(A_{N,\varepsilon}^c(h)-A_{N,\varepsilon}(h)\bigr).
\]
沿用已经证明的周期系数公式，其 \(p\) 轴系数为
\[
\rho_p^{|a|}
\bigl(J_{p,\varepsilon}(-aL)-L\bigr).
\]

因为 \(L/M\) 无理，\(-L\notin M\mathbb Z\)。可以固定一个与
\(\varepsilon\) 无关的 \(h\in C_c^\infty\)，使其支集足够靠近 \(-L\)，满足
\[
h(-L)=1,
\]
并避开 \(0\)、其余 \(p\) 周期点及全部 \(q\) 周期点。于是
\[
\Delta_\varepsilon(h)
=\rho_p\bigl(J_{p,\varepsilon}(-L)-L\bigr)
\longrightarrow0.
\tag{21}
\]
而目标边界差
\[
B_{p,q}(h)=-L P_p(h)+M P_q(h)
\]
对此测试为
\[
B_{p,q}(h)=-L\rho_p\ne0,
\]
其相反数也非零。因此
\[
\Delta_\varepsilon=\pm B_{p,q}
\]
不可能对全部合法分割成立。事实上，由显式界 (1)，所有充分小的
\(\varepsilon\) 都满足
\[
|\Delta_\varepsilon(h)|<\frac12L\rho_p,
\]
从而在这个固定测试上同时排除两个符号。

若使用未取 \(1/2\) 的完整迹差，只需在 (21) 左右乘 \(2\)；趋零结论及排除结果不变。此论证也不需要控制 \(J_q\)，因为所选测试已经避开全部 \(q\) 周期。

排除范围仅是：**把这一原连接演化产生的直接迹差，未经其他新结构修正，就认作对所有合法分割成立的固定边界补偿。** 不排除其他连接、附加结构或不同相对迹机制。
