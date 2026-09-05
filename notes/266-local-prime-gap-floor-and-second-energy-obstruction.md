# 266. 实际局部素数间隙能量下界与二阶预算障碍

日期：2026-09-05。路线：NCE-8 / B1u，辅助线。
论文归属：Vaughan--Brownian response；本轮仅Markdown。

状态：[T] 实际局部balanced primitive的质量无关下界；
[T] 局部mass-only预算的必要质量分离尺度；
[N] 光滑正源中二阶预算不推出四阶预算的显式反例；
[E] 四个固定dyadic窗口的局部质量和能量复算。
没有证明实际dyadic预算失败，也没有从有限实验推出渐近增长。

## 1. 间隙方差引理 [T]

设实函数 \(f\) 在长度为 \(\ell>0\) 的区间 \(J\) 上绝对连续，
并且 \(f'\le-g_0<0\) 几乎处处。则
\[
 \boxed{\ \int_J|f|^2\ge\frac{g_0^2\ell^3}{12}.\ }
 \tag{1}
\]
证明：令 \(\bar f=\ell^{-1}\int_J f\)。由
\(|f(x)-f(y)|\ge g_0|x-y|\) 及方差恒等式，
\[
 \int_J f^2\ge\int_J(f-\bar f)^2
 =\frac1{2\ell}\int_J\int_J(f(x)-f(y))^2dx\,dy
 \ge\frac{g_0^2}{2\ell}\frac{\ell^4}{6}.
 \tag{2}
\]
取 \(f\) 为过区间中心零点的斜率 \(-g_0\) 直线时取等。\(\square\)

此下界不需要知道区间左端的累计差，故不同prime gaps之间未知的符号与常数
不能消除它。但它只控制一个二阶能量，不等于响应下界。

## 2. 实际局部源的二阶下界 [T]

取与265完全相同的实际Abel源，允许任意有限 \(N\ge Y\)，
固定 \(0<\sigma<1,\ a=1-\sigma,\ L=\log Y\)。
令 \(I_H=[L-H,L+H]\)，并要求
\[
 \log2\le H<L/6.
 \tag{3}
\]
用 \(\alpha_H,\beta_H\) 表示限制，质量为 \(A_H,B_H\)，
\(M_H=A_H-B_H\)，并在offset \(u=\lambda-L\) 上定义
\[
 \zeta_H=\alpha_H-(A_H/B_H)\beta_H,\quad
 E_{1,H}=\|F_{\zeta_H}\|_2^2,\quad
 E_{2,H}=\|F_{\zeta_H*\zeta_H}\|_2^2.
 \tag{4}
\]
能量不受平移影响。这里的 \(\zeta_H\) 是测度而不是zeta函数。

### 定理266-A

对全部充分大 \(Y\)、所有上述 \(N,H\)，有
\[
 \boxed{\ E_{1,H}\ge c_\sigma Y^{-2\sigma}(\log Y)^2.\ }
 \tag{5}
\]
下界不依赖 \(M_H\)，特别地在 \(M_H=0\) 处仍严格为正。

证明：固定bulk区间
\(J=[\log(Y/2),\log Y]\)，它被(3)保证包含在局部源支撑内。
定性PNT给 \(\psi(Y)-\psi(Y/2)\ge Y/4\) 于充分大 \(Y\)，因此
\[
 A_H\ge e^{-1}Y^{-\sigma}
          \sum_{Y/2<n\le Y}\Lambda(n)\ge c_\sigma Y^a.
 \tag{6}
\]
连续积分给 \(B_H\le\Gamma(a)Y^a\)。所以 \(q=A_H/B_H\ge c_\sigma>0\)。
同时 \(A_H\le A\ll Y^a\)、\(B_H\ge b_\sigma Y^a\)，也有 \(q\ll_\sigma1\)。
这些只使用源的PNT/bulk信息，而不使用质量差。

在 \(J\) 的任何无prime-power原子开间隙上，\(f=F_{\zeta_H}\) 的导数为
\[
 f'(\lambda)=-q e^{a\lambda-e^\lambda/Y}\le-c_\sigma Y^a.
 \tag{7}
\]
\(J\) 中不同prime-power原子总数 \(r\) 满足
\[
 r\le\frac{\psi(Y)}{\log(Y/2)}
       +\sqrt Y\,\log_2Y\le C\frac Y{\log Y}.
 \tag{8}
\]
第一项上界该bulk中的素数数目，第二项粗略覆盖所有指数至少2的prime powers；
多计和重复只使上界更大。后一步只用 \(\psi(Y)\ll Y\) 及
\(\sqrt Y\log Y=o(Y/\log Y)\)。

将 \(J\) 按这些原子分成至多 \(r+1\) 个开间隙，长度 \(\ell_j\) 之和为 \(\log2\)。
端点的零测集不影响能量。由(1)及Jensen，
\[
 E_{1,H}\ge c_\sigma Y^{2a}\sum_j\ell_j^3
 \ge c_\sigma Y^{2a}\frac{(\log2)^3}{(r+1)^2}
 \ge c_\sigma Y^{-2\sigma}L^2.
 \tag{9}
\]
\(\square\)

此证明不使用任何未证的最大素数间隙、素数对相关或RH。
这是可审计但较小的下界；它随 \(Y\) 衰减，不能解释有限数据中的大能量。

### 推论266-B：局部预算所需的质量尺度

264的最优不等式和(5)给
\[
 E_{2,H}\ge c_\sigma\frac{Y^{-4\sigma}L^4}{H}.
 \tag{10}
\]
因此，若某个实际cofinal局部族在 \(M_H\ne0\) 点满足统一
\(J_{\rm loc}\le C(M_H/S_H)^4\)，则
\[
 \boxed{\ |M_H|\ge c_{\sigma,C}Y^{-\sigma}L^{3/4}H^{-1/4}.\ }
 \tag{11}
\]
证明：264-(19)给
\(E_{2,H}\le(8C+44000)LM_H^4\)，与(10)结合。\(\square\)

若同一不等式还被要求用于 \(M_H=0\)，则(5)、264-A及260平衡定理直接排除它。
若另外证明 \(|M_H|\le C_0|M|\)，(11)也给full质量同阶必要下界。
但这里没有证明实际所选dyadic质量会低于(11)，故不是对该schedule的no-go。
它也不取代262的full-source必要条件：二者的前提和响应对象不同。

## 3. 仅二阶能量不足：光滑正源反例 [N]

取固定 \(L=4,H=1/2\)，写 \(t=u+1/2\in[0,1]\)。
对每个整数 \(n\ge1\)，令
\[
 d\beta_n=dt,\qquad
 d\alpha_n=(1+n^{-1}+\cos(2\pi nt))dt .
 \tag{12}
\]
这两源严格为正，physical lag为 \(L+u\)，且 \(L>6H\)。
有 \(A_n=1+n^{-1}, B_n=1, M_n=n^{-1}\)，balanced discrepancy为
\[
 d\zeta_n=\cos(\omega t)dt,\qquad \omega=2\pi n.
 \tag{13}
\]
它质量为零。直接积分得
\[
 \boxed{\ E_{1,n}=\frac1{2\omega^2},\qquad
 E_{2,n}=\frac1{12\omega^2}-\frac1{8\omega^4}.\ }
 \tag{14}
\]

证明：\(F_{\zeta_n}(t)=\sin(\omega t)/\omega\) 于 \(0<t<1\)，其余为0。
把卷积坐标平移为 \(s\in[0,2]\)，则于 \(0<s<1\)
\[
 (\zeta_n*\zeta_n)(s)
 =\frac s2\cos(\omega s)+\frac{\sin(\omega s)}{2\omega},
 \qquad
 F_{\zeta_n*\zeta_n}(s)=\frac{s\sin(\omega s)}{2\omega}.
 \tag{15}
\]
卷积密度关于 \(s=1\) 对称且总质量为0，故primitive满足 \(F(2-s)=-F(s)\)。
原offset卷积坐标为 \(s-1\)，平移不改变能量。
于是
\[
 E_{2,n}=\frac1{2\omega^2}\int_0^1s^2\sin^2(\omega s)ds
 =\frac1{2\omega^2}\left(\frac16-\frac1{4\omega^2}\right),
 \tag{16}
\]
即(14)。\(\square\)

此族满足264所要求的更强二阶预算，事实上
\[
 \frac{E_{1,n}}{M_n^2\sqrt{LH}}=\frac1{8\pi^2\sqrt2},
 \qquad
 \frac{E_{2,n}}{LM_n^4}
 =\frac{n^2}{192\pi^2}-\frac1{512\pi^4}\longrightarrow\infty .
 \tag{17}
\]
由264-C，\(J_{{\rm loc},n}/(M_n/S_n)^4\to\infty\)。
这严格排除“二阶预算小便足以闭合四阶响应”的一般推理。
也可令 \(L_n=4+(\log n)^2\)、\(H=1/2\)；
这时仍满足二阶预算，而 \(E_{2,n}/(L_nM_n^4)\to\infty\)。
所以即使另加 \(L\to\infty\)，这个逻辑缺口也不会消失。

此例不是von Mangoldt系数，也不满足全部实际Abel算术假设。
它只说明265的一份signed primitive saving不能由正源和几何自动变成两份saving；
实际(24)仍必须依靠新的算术信息。

## 4. 实际局部窗口的冻结复算 [E]

运行 `python -B scripts/local_balanced_energy_probe.py`，固定
\(\sigma=1/4,Y=2^m,N=\lfloor Y(\log Y)^2\rfloor\)。
所测 \(m=6,10,14,18\) 上，候选宽度 \(L/8\) 与 \(\min(\log L,L/8)\)
恰好相同；脚本去重后只算四个窗口，不把它们记为八个不同实验。
各窗均满足 \(0<H<L/6\)；最小 \(m=6\) 不满足(3)的 \(H\ge\log2\)，
因此不能套用定理266-A，但满足264的局部模型条件。

| \(m\) | 局部prime-power数 | \(M_H/M\) | \(E_{1,H}\) | \(E_{1,H}/(M_H^2\sqrt{LH})\) |
|---:|---:|---:|---:|---:|
| 6 | 19 | -0.137297 | 0.054815 | 3.649954 |
| 10 | 294 | -1.486659 | 0.841362 | 0.273344 |
| 14 | 4996 | -3.058169 | 5.965838 | 0.326185 |
| 18 | 90813 | -1.852260 | 12.727880 | 1.475169 |

局部归一化比不单调；表格既不证明渐近发散，也不证明预算成立。
6/10阶Gaussian结果相对差至多 \(1.15\cdot10^{-13}\)；
最大累计平衡残差约 \(1.82\cdot10^{-12}\)，均不是interval误差认证。
最小例另用试除生成系数、50位不完全Gamma原函数和自适应积分，
得到 \(E_{1,H}=0.0548146691100414671190738\)，
与向量化算法相对差约 \(7.72\cdot10^{-15}\)。
本机longdouble只有52个显式尾数位。所有数值仍是[E]。

## 5. 公理用途、循环性与下一步

实际下界只使用：正continuum bulk、定性PNT确保非消失局部质量比、
prime-power原子的计数上界、间隙上的绝对连续primitive，以及264的已证局部响应判据。
删除原子计数约束后，过密原子可使间隙下界退化；
删除 \(H\ge\log2\) 后固定bulk不再保证位于窗口；
删除正连续密度或质量比下界后(7)失效。
这些是证明的失效位置，不都声称已有反例。

反例(12)满足实正性、carrier分离和二阶预算，精确删除的是独立四阶算术输入。
它没有使用未知零点，也没有把Weil正性或负指数当作公理。
一维能量工具可移植；复系数和Gamma-complete响应仍须独立桥梁。

下一最小引理仍为265-(24)中的实际四份差异卷积预算。
本轮实际gap下界只作为指定局部schedule的必要性测试；
当前浮点样本不触发停止该schedule的结论。
间隙方差及三角函数计算是经典工具；内部证明与独立复核不等于新颖性已认证。
