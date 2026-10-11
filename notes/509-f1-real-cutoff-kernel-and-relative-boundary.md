# 509. 实位双截止原核、迹类边项与零电荷检验

2026-10-11。[T/R/N] 继续[508的实位间隙测试](508-f1-prime-gap-archimedean-mixed-test.md)。
本稿计算实际实位硬截止及一个 Gaussian 对照，给出迹类准入和定量比较。
最直接的双截止相对闭链虽合法，电荷仍为零；[510](510-f1-real-fourier-inversion-relative-cycle.md)随后采用新的实际反演边。
局部 Hilbert 空间不是[404](404-f1-adelic-periodic-orbits-and-mixed-local-trace.md)半局部商空间的已证直和分量。

## 1. 固定作用与两个实符号

在 \(\mathcal H=L^2(\mathbb R,dx)\) 中取
\[
 \mathcal F\xi(y)=\int_{\mathbb R}\xi(x)e^{-2\pi ixy}dx,\qquad
 d^\times w=\frac{dw}{2|w|},\qquad
 S_w\xi(x)=\xi(wx),\quad U(w)=S_{w^{-1}}.                 \tag{1}
\]
\(\|S_w\|=|w|^{-1/2}\)，故 \(U(w)\) 并非酉表示。
对 \(f\in C_c^\infty(\mathbb R)\)，实际有界表示积分为
\[
 T_f=\int f(\log|w|)U(w)d^\times w
     =\int f(-\log|a|)S_a d^\times a.                    \tag{2}
\]
两实符号各占一半 Haar 权重。直接变元给
\[
 T_f^*=T_{\overline f^\sharp},\qquad
 \mathcal F T_f\mathcal F^{-1}=T_{f^\sharp},\qquad
 f^\sharp(t)=e^{-t}f(-t).                                \tag{3}
\]
508的 \(h=h^\sharp\) 实函数使 \(T_h\) 自伴且与 \(\mathcal F\) 交换。
这不保证其 Fourier 乘子非负。

本稿根线程与独立审查均回读固定
[Connes v1](../literature/f1/connes-trace-math-9811068v1.pdf) PDF21–23的Theorem3、
PDF29–32的半局部来源及Theorem4；前者使用的确是(1)的非酉作用。
单位元正规化仍按[405](405-f1-adelic-restriction-moments-and-radical.md)。

## 2. 硬截止本身的迹类性

令
\[
 P_\Lambda=M_{\mathbf1_{[-\Lambda,\Lambda]}},\qquad
 Q_\Lambda=\mathcal F^{-1}P_\Lambda\mathcal F,\qquad
 R_\Lambda=Q_\Lambda P_\Lambda.                          \tag{4}
\]
偶截止使 \(Q_\Lambda=\mathcal F P_\Lambda\mathcal F^{-1}\)，符合原文。
\(R_\Lambda\) 是两个投影的乘积，通常不是投影。

先证明迹类，再计算核迹。有限矩形算子
\(A=P_\Lambda\mathcal F P_\Lambda\) 的核有 rank-one 展开
\[
 \mathbf1_{[-\Lambda,\Lambda]}(\xi)\mathbf1_{[-\Lambda,\Lambda]}(x)
 \sum_{n\ge0}\frac{(-2\pi i)^n}{n!}\xi^n x^n.             \tag{5}
\]
第 \(n\) 项的迹类范数是
\[
 \frac{(2\pi)^n}{n!}\frac{2\Lambda^{2n+1}}{2n+1}.
\]
总和至多 \(2\Lambda e^{2\pi\Lambda^2}<\infty\)；
故 \(A\) 以及 \(R_\Lambda=\mathcal F^{-1}A\) 都属于 \(\mathcal S_1\)。
因 \(S_a\) 有界，\(R_\Lambda S_a,R_\Lambda T_f\in\mathcal S_1\)。
在紧乘法参数集上，迹类范数由
\(\|R_\Lambda\|_1|a|^{-1/2}\) 控制，允许在 \(\mathcal S_1\) 中积分。

## 3. 原核与显式余项

\(Q_\Lambda\) 的核为
\[
 r_\Lambda(x-y)=\frac{\sin(2\pi\Lambda(x-y))}{\pi(x-y)}.
\]
因此
\[
 (R_\Lambda S_a)(x,y)=|a|^{-1}r_\Lambda(x-y/a)
                           \mathbf1_{\{|y/a|\le\Lambda\}}. \tag{6}
\]
从(5)的绝对收敛展开取迹，得到
\[
 \operatorname{Tr}(R_\Lambda S_a)
 =\int_{-\Lambda}^{\Lambda}\int_{-\Lambda}^{\Lambda}
                  e^{2\pi i(a-1)x\xi}d\xi dx
 =\frac{2\operatorname{Si}(2\pi(a-1)\Lambda^2)}
            {\pi(a-1)}=:I_\Lambda(a-1),                 \tag{7}
\]
其中 \(I_\Lambda(0)=4\Lambda^2\)，
\(\operatorname{Si}(z)=\int_0^z\sin u/u\,du\)。
对 \(c\ne0\)，分部积分给
\[
 \left|I_\Lambda(c)-|c|^{-1}\right|
       \le\frac{2}{\pi^2c^2\Lambda^2}.                  \tag{8}
\]
这不是用平迹分布替代普通算子迹。

若 \(h\) 支集离开0，则 \(h(-\log|a|)\) 支集离开 \(a=1\)，于是
\[
 \left|\operatorname{Tr}(R_\Lambda T_h)-L_\infty(h)\right|
 \le\frac{2}{\pi^2\Lambda^2}
     \int\frac{|h(-\log|a|)|}{|1-a|^2}d^\times a,
 \quad
 L_\infty(h)=\int\frac{h(-\log|a|)}{|1-a|}d^\times a.     \tag{9}
\]
分别变换正、负参数并平均，
\[
 L_\infty(h)=\int_0^\infty
    \frac{e^{2t}h(t)+e^t h(-t)}{e^{2t}-1}dt.
\]
对实 sharp 不变的508测试，
\[
 \lim_{\Lambda\to\infty}\tfrac12\operatorname{Tr}(R_\Lambda T_h)
  =\mathcal A_\infty(h)
  :=\int_0^\infty\frac{e^{2t}h(t)}{e^{2t}-1}dt>0.        \tag{10}
\]
这个二分与404一致。原 \(U(w)\) 的单参数极限为
\(|w|/|1-w|\)；只有换成 \(a=w^{-1}\) 后才是 \(|1-a|^{-1}\)。

## 4. Gaussian 对照只比较当前离单位元测试

另取实际正压缩
\[
 P_R^G=M_{e^{-\pi x^2/R^2}},\qquad
 Q_R^G=\mathcal F^{-1}P_R^G\mathcal F,\qquad R_R^G=Q_R^GP_R^G.
\]
它们不是硬投影。直接 Gaussian Fourier 积分给 Schwartz 核
\[
 (R_R^G S_a)(x,y)=\frac R{|a|}
  \exp[-\pi R^2(x-y/a)^2-\pi(y/a)^2/R^2].
\]
故其算子确实迹类，且
\[
 \operatorname{Tr}(R_R^G S_a)=((1-a)^2+R^{-4})^{-1/2},
 \qquad \|R_R^G S_a\|_2^2=\frac{R^2}{2|a|}.             \tag{11}
\]
离 \(a=1\) 的误差至多 \(R^{-4}/(2|1-a|^3)\)。
因此在(9)的测试上，两个实际读出的差至多
\[
 \frac{R^{-4}}2\int\frac{|h(-\log|a|)|}{|1-a|^3}d^\times a
 +\frac{2}{\pi^2\Lambda^2}
       \int\frac{|h(-\log|a|)|}{|1-a|^2}d^\times a.       \tag{12}
\]
没有把这项标量比较推广为迹类范数比较，也没有据此识别一般测试的单位元常数。

## 5. 积分才使这些直接边项迹类

当 \(|a|\ne1\)，
\[
 [P_\Lambda,S_a]=
   M_{\mathbf1_{\{|x|\le\Lambda\}}-\mathbf1_{\{|ax|\le\Lambda\}}}S_a
\]
是非零正测度环带乘法与可逆缩放的复合，非紧；Fourier侧同样如此。
不能把单参数边项注册为迹类。\(a=-1\) 与偶截止交换，是明确例外。

但是 \([P_\Lambda,T_f]\in\mathcal S_1\)。其核为
\[
 (\mathbf1_{\{|x|\le\Lambda\}}-\mathbf1_{\{|y|\le\Lambda\}})
                \frac{f(\log|x/y|)}{2|y|}.              \tag{13}
\]
若 \(\operatorname{supp} f\subset[-M,M]\)，非零核满足
\(e^{-M}\Lambda\le |x|,|y|\le e^M\Lambda\)。
在这个远离坐标轴的紧矩形外选光滑截止，未乘示性函数的核是光滑紧支核，
对应一个迹类算子 \(B\)。(13)就是 \(P_\Lambda B-BP_\Lambda\)，因此
\[
 \operatorname{Tr}[P_\Lambda,T_f]=0,\qquad
 [Q_\Lambda,T_f]\in\mathcal S_1,\quad
 \operatorname{Tr}[Q_\Lambda,T_f]=0.                     \tag{14}
\]
后一式由(3)得到。这些是合法但不能单独支付(10)的边项。

## 6. 一条真实双截止闭链仍有零电荷

在包含这些有界算子和 \(\mathcal S_1\) 的实际代数中按 \(\mathcal S_1\) 取商。
\(q(R_\Lambda)=0\)，所以把 \(R_\Lambda\) 直接作张量因子不能产生非零商链。
保留两个独立硬投影的候选
\[
 c_\Lambda=q(P_\Lambda)\otimes q(Q_\Lambda T_h)           \tag{15}
\]
确实闭合，因为
\[
 P_\Lambda Q_\Lambda T_h\in\mathcal S_1,\qquad
 Q_\Lambda T_hP_\Lambda
   =Q_\Lambda P_\Lambda T_h+Q_\Lambda[T_h,P_\Lambda]\in\mathcal S_1.
\]
两个顺序乘积均迹类，循环迹恒等式给
\(\Omega(c_\Lambda)=\operatorname{Tr}[P_\Lambda,Q_\Lambda T_h]=0\)。
这里不能误用于仅交换子迹类、两个乘积自身非迹类的候选；510正采用后一机制。

此外 \(T_h\) 在偶子空间的酉对数坐标
\(\psi(u)=\sqrt2e^{u/2}\xi(e^u)\) 中是非零平移不变卷积算子；
奇子空间被符号平均消去。非零 Fourier 乘子在正测度集上非零，
用平移弱趋零的单位向量可证该算子非紧。
硬与 Gaussian 截止均强趋单位，故截止后的算子强趋非紧 \(T_h\)；
它们不能在迹类范数中收敛。收敛标量迹不许可无限链的迹类转移。

## 7. 本轮结果与后续边界

本稿支付实际局部硬核、迹类准入、离单位元误差、Gaussian比较和积分边项；
不提供有限 \(S\) 商空间的新增分解。404的Theorem4仍给
\(S=\{\infty,2,5\}\) 的整体截止读出，其中508测试的两个有限位项为零。
真正新的非零实位闭链见510；其有限 \(S\) 提升必须另证。
单位元、混合主关系、全测试类正性和RR不能由(10)自动取得。
