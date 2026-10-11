# 521. 移动真实源校准与全高度统一预解界

2026-10-11。[T/R] 接续[518](518-f1-quantitative-mellin-division-and-mobius-source.md)、
[519](519-f1-closed-source-image-and-degree-moments.md)、
[520](520-f1-source-quotient-spectrum-and-centered-growth.md)。
本稿解决520固定Gaussian校准在无限高度可能产生的Gamma指数损失。
使用同一个合法源空间的复化，构造随预解参数移动的实际源；
在零点所在条带之外支付统一半范数，未取得新的无零区域。

## 1. 原空间、半范数与右侧零点边界

仍取
\[
 X=\mathcal S_{\exp,\mathbb C}/I_{\mathbb C},\qquad
 I_{\mathbb C}=\mathcal R_{\rm jet,\mathbb C},\qquad B=A-\tfrac12,
 \quad A=-D.
\]
对整数 \(n\ge1\)，先在原空间取有限最大值，再取商：
\[
 P_n(f)=\max_{0\le N,j\le n}p_{N,j}(f),\qquad
 \bar P_n([f])=\inf_{i\in I_{\mathbb C}}P_n(f+i).             \tag{1}
\]
这些递增商半范数定义X的Fréchet拓扑；
没有对每一项分别选择不同代表元。

令
\[
 b=\sup_\rho\Re\rho,\qquad Z(s)=(s-1)\zeta(s).
\]
经典临界条带及函数方程给 \(1/2\le b\le1\)。
Z整，在 \(\Re s>b\) 无零点，且 \(Z(1)=1\)；
其平凡零点位于负实轴。
下文固定
\[
 b<d_0\le\Re\lambda\le S,\qquad S<\infty.                   \tag{2}
\]
所有常数、半范数下标只依赖n及这个固定条带，均不依赖虚部高度。
若只知道全部零点位于 \([a,b_0]\)，可使用任意 \(d_0>b_0\)，
没有把该条带假设当成已经证明的算术结论。

## 2. 没有Gamma分母的合法移动源

固定 \(\psi\in C_c^\infty((1,2),\mathbb R)\)，满足
\[
 \int_0^\infty\psi(r)\frac{dr}{r}=1.
\]
在r>0定义，再作偶延拓：
\[
 \theta_\lambda(r)=(r\partial_r+1)\bigl(r^{-\lambda}\psi(r)\bigr),
 \qquad \theta_\lambda(-r)=\theta_\lambda(r).               \tag{3}
\]
这是复偶Schwartz函数，支集远离0，且
\[
 \theta_\lambda(0)=0,\qquad
 \int_{\mathbb R}\theta_\lambda(r)dr
 =2\int_0^\infty\partial_r\bigl(r^{1-\lambda}\psi(r)\bigr)dr=0.
\]
故它进入519原合法源空间的复化，没有删除任一原准入条件。

记
\[
 J_\psi(u)=\int_0^\infty r^u\psi(r)\frac{dr}{r},\quad
 h_\lambda=E\theta_\lambda\in I_{\mathbb C}.
\]
正实Mellin分部积分与实际E映射给
\[
 M_+\theta_\lambda(s)=(1-s)J_\psi(s-\lambda),\qquad
 M_{h_\lambda}(s)=-2Z(s)J_\psi(s-\lambda).                  \tag{4}
\]
后一等式先在 \(\Re s>1\) 由绝对换序成立，再由两边整性延拓。
因 \(J_\psi(0)=1\)，准确校准为
\[
 c_\lambda:=M_{h_\lambda}(\lambda)=-2Z(\lambda)\ne0.        \tag{5}
\]
特别 \(c_1=-2\)，在λ=1没有极或归一化失败。
(3)随λ在源Fréchet空间中整依赖，hλ同样整依赖。
分母(5)没有完成函数的Gamma因子。

## 3. 全高度多项式逆界，不使用零点间距

先支付
\[
 \sup_{d_0\le\sigma\le S}
       |Z(\sigma+iT)|^{-1}\le C(1+|T|)^L,
                         \qquad T\in\mathbb R,             \tag{6}
\]
其中L有限，只依赖(2)。

取 \(r=\min((d_0-b)/4,1/4)\)，
\(\sigma_*=\max(2,S+1)\)。
从 \(\sigma_*+iT\) 到任意 \(\sigma+iT\) 的水平线段，
可用至多
\[
 J=\left\lceil(\sigma_*-d_0)/r\right\rceil+1
\]
个步长至多r的移动连接。
每一步所在半径2r圆盘位于 \(\Re s>b\)，故Z无零。
所有圆盘处于同一固定实部带。

[NIST DLMF 25.2.8](https://dlmf.nist.gov/25.2#E8)的N=1式给，
在固定正实部带内
\[
 Z(s)=s-s(s-1)\int_1^\infty
                 \frac{x-\lfloor x\rfloor}{x^{s+1}}dx.
\]
该积分绝对值至多 \(1/\Re s\)，故在上述圆盘联合上
\[
 |Z(s)|\le M_T:=C_0(1+|T|)^2.                              \tag{7}
\]
C0可增大以同时保证 \(M_T\ge1\)。
绝对Euler逆在锚点给
\[
 |Z(\sigma_*+iT)|
 \ge\frac{|\sigma_*-1+iT|}{\zeta(\sigma_*)}
 \ge c_0:=\frac{\sigma_*-1}{\zeta(\sigma_*)}>0.              \tag{8}
\]

\(u(s)=\log M_T-\log|Z(s)|\) 是每个无零圆盘上的非负谐函数。
由Poisson核，上述圆盘内距中心至多r处，
u至多中心值的3倍。
沿有限链迭代得到
\[
 u(\sigma+iT)\le3^J(\log M_T-\log c_0),
\]
所以
\[
 |Z(\sigma+iT)|
 \ge M_T^{\,1-3^J}c_0^{\,3^J}.
\]
例如 \(L=2(3^J-1)\) 即支付(6)，无需优化这个粗指数。
这是全部高度的估计；λ=1由整函数Z直接处理。
常数在 \(d_0\downarrow b\) 时可能恶化，
因此不据此声称零点边界线上也有同样估计。

## 4. 移动源的明确目标半范数成本

固定(2)，任意普通源Schwartz半范数满足
\[
 Q_{a,j}(\theta_\lambda)
       \le C_{a,j}(1+|T|)^{j+1},\qquad T=\Im\lambda,
\]
因为源支集固定于 \(1\le|r|\le2\)，每次普通微分只增加有限个λ因子。
还可直接由Poisson求和支付明确目标界
\[
 P_n(h_\lambda)\le C_n(1+|T|)^{2n+3}.                     \tag{9}
\]

对 \(t\ge0\)，E和在 \(t>\log2\) 恒零，
在剩余紧区间只含有限项，导数成本至多 \(j+1\) 阶λ多项式。
对 \(t<0\)，设 \(r=e^t\le1\)，原准入两项使Poisson公式成为
\[
 h_\lambda(t)=2r^{-1}
                    \sum_{m\ge1}\widehat\theta_\lambda(m/r). \tag{10}
\]
使用405的自对偶Fourier约定。
\(D_t^j\) 在每项上给
\(r^{-1}(-1-y\partial_y)^j\widehat\theta_\lambda(y)\)，
其中 \(y=m/r\)。
取 \(K=n+2\)，Fourier分部积分给，对 \(0\le j\le n\)，
\[
 |(-1-y\partial_y)^j\widehat\theta_\lambda(y)|
 \le C_{n,j}(1+|T|)^{K+j+1}y^{-K},\qquad y\ge1.
\]
这里只需要源普通导数至K+j：
对展开后的 \(y^\ell\widehat\theta_\lambda^{(\ell)}(y)\)，
对 \(r^\ell\theta_\lambda(r)\) 分部积分K+ℓ次即可。
于是(10)的j阶导数至多
\[
 C(1+|T|)^{K+j+1}r^{K-1}\zeta(K).
\]
乘 \(r^{-n}\) 后仍有界，且 \(K+j+1\le2n+3\)，证明(9)。
没有将无限高度的成本藏入随λ变化的半范数。

## 5. 实际预解及统一 \(1/(1+|T|)\) 界

对 \(f\in\mathcal S_{\exp,\mathbb C}\) 令
\[
 v_\lambda(f)=f-\frac{M_f(\lambda)}{c_\lambda}h_\lambda,
 \qquad M_{v_\lambda(f)}(\lambda)=0.                        \tag{11}
\]
使用520的一阶实际积分算子
\[
 R_\lambda v(t)=e^{-\lambda t}\int_{-\infty}^t e^{\lambda u}v(u)du
              =-e^{-\lambda t}\int_t^\infty e^{\lambda u}v(u)du.
\]
则 \((D+\lambda)R_\lambda v=v\)。
设 \(z=\lambda-\tfrac12\)，定义
\[
 \mathcal R(z)[f]=[R_\lambda v_\lambda(f)].
\]
因hλ在原源像I中、且除以 \(\lambda-s\) 在每个ρ处是单位，
该式良定义于X，并且
\[
 \boxed{\mathcal R(z)=(z-B)^{-1},\qquad \Re z>b-\tfrac12.}   \tag{12}
\]
单射与双侧逆仍由520的完整jets单位论证支付。
式(11)保持I，未添加目标双次数条件。

关键是对每个n，存在一个固定m及C，使
\[
 \boxed{\bar P_n(\mathcal R(\sigma+iT)x)
       \le\frac{C}{1+|T|}\bar P_m(x),\qquad
 d_0-\tfrac12\le\sigma\le S-\tfrac12,\quad T\in\mathbb R.}  \tag{13}
\]
证明如下。固定整数 \(k>n+S\)。
在零λ矩子空间上，D与Rλ交换，
因为分部积分给
\[
 R_\lambda Dv=(R_\lambda v)'.
\]
两端尾积分估计故给
\[
 P_n(R_\lambda v)\le C P_k(v),\qquad
 P_n(R_\lambda Dv)\le C P_k(Dv).
\]
由微分方程及λ≠0，
\[
 R_\lambda v=\frac v\lambda-\frac{R_\lambda Dv}{\lambda},
 \quad
 P_n(R_\lambda v)\le\frac C{|\lambda|}
                         \bigl(P_k(v)+P_k(Dv)\bigr).        \tag{14}
\]
\(M_{Dv}(\lambda)=-\lambda M_v(\lambda)=0\)，故第二项合法；
这里不采用会额外产生虚部幂次的粗导数递推。

任意固定实部带内，518的分部积分对所有整数q给
\[
 |M_f(\lambda)|\le C_q(1+|T|)^{-q}P_{m_q}(f),
\]
其中 \(m_q\ge\max(q,\lceil S\rceil+1)\) 可固定。
用(6)、(9)和 \(P_k(Dv)\le P_{k+1}(v)\)，
取 \(q\ge L+2k+5\)，支付
\[
 P_{k+1}(v_\lambda(f))\le C P_m(f)
\]
的全高度统一界，m只依赖n和(2)。
又 \(\Re\lambda\ge d_0>1/2\) 保证
\(1/|\lambda|\le C/(1+|T|)\)，故(14)给原空间界。
最后对f+i整体取(1)的下确界，得到(13)。

式(12)在整个右侧无零半平面是X值全纯族：
源与校准分母全纯，尾积分在参数紧集上具有统一指数衰减，
逐参数微分的多项式尾因子由增加一个固定指数权控制。
因此(13)还可用于固定条带内的严格预解轮廓移动。

## 6. 付清的范围与下一步

本稿支付了真实源修正、全高度有限半范数控制和预解衰减。
零点限制在某条带是(6)所需输入，没有据预解构造证明更窄零点条带。
特别不能把 \(b=1/2\) 在本稿中当成无条件事实。

[522](522-f1-optimal-centered-growth-and-rh-equivalence.md)将(13)与商半范数的
Banach完成、原平移的粗指数界及二阶正则化Bromwich公式相接，
证明520的增长合同与RH等价，并确定增长指数下确界。
这个等价准确说明增长关口携带的算术内容，
不提供独立Weil符号、Hilbert酉化、全局HH桥或新的RH证明。
