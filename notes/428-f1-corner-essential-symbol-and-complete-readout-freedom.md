# 428. 固定正角的精确本质符号与全部受限读出的自由度

2026-10-04。接续[427](427-f1-corner-product-algebra-and-unavoidable-trace-cocycle.md)的实际乘法代数。
本稿精算本质范数、完整符号商和426受限相容读出的全部自由度。
它证明源T在该商中仅作用为单位，既有受限循环条件无法限制时间分布；原物理周期读出也不连续于符号的一致范数。
没有据此否定其他更大的几何或相对循环域。

## 1. 同一个平滑frame及其右端

沿用427的 \(A(h)=VU(h)V^*\)、\(V^*V=M_m\)，其中
\(0\le m\le2\)，充分负端m=0，充分正端m=2。
取任意单位 \(\psi\in C_c^\infty(\mathbb R)\)，令 \(\psi_j(x)=\psi(x-j)\)，j趋于正无穷。
充分大的j使 \(\psi_j\) 和 \(U(h)\psi_j\) 的支集都进入m=2区间；后者紧支来自h与ψ紧支。
设
\[
                         \xi_j=V\psi_j/\sqrt2.              \tag{1}
\]
于是 \(\|\xi_j\|=1\)，且 \(\xi_j\rightharpoonup0\)，因为 \(\psi_j\) 弱趋零、V有界。
由原frame公式，
\[
 A(h)\xi_j=\sqrt2VU(h)\psi_j,\qquad
                         \|A(h)\xi_j\|=2\|U(h)\psi\|.       \tag{2}
\]
任何紧算子在 \(\xi_j\) 上范数趋零。因此取所有单位紧支光滑ψ的上确界，得到
\[
 \|A(h)\|_{\rm ess}\ge2\|U(h)\|,
 \qquad \|A(h)\|\le\|V\|^2\|U(h)\|=2\|U(h)\|.             \tag{3}
\]
这些ψ在L²稠密，足以逼近有界算子范数。
Plancherel给 \(\|U(h)\|=\|\widehat h\|_\infty\)，故
\[
             \boxed{\|A(h)\|_{\rm ess}=\|A(h)\|
                                  =2\|\widehat h\|_\infty.} \tag{4}
\]
由Fourier单射性，\(A(h)\) 紧当且仅当 \(h=0\)，因此也有
\(A(h)\in\mathcal S_1\iff h=0\)。
这比426的迹类交集零迹结论更强；证明始终使用原平滑分割。

## 2. 实际符号商及其C*完成

\(\mathcal D=A(C_c^\infty)\oplus\mathcal S_1\) 是代数直和的线性分解，由(4)唯一。
定义
\[
 \operatorname{symb}(A(h)+S)=2\widehat h.                     \tag{5}
\]
427的 \(A(h)A(k)=2A(h*k)+\mathcal S_1\) 证明它是星代数满射到
\(\mathcal B=2\widehat{C_c^\infty(\mathbb R)}\)，核恰为 \(\mathcal S_1\)。
因为因子2已包含于符号，商乘法就是逐点乘法。
对于 \(F=A(h)+S\)，
\[
       \|F+\mathbb K(\mathcal H)\|=2\|\widehat h\|_\infty.   \tag{6}
\]
S₁在紧算子中算子范数稠密，所以在 \(\mathcal D/\mathcal S_1\) 上由算子范数得到的商范数也是(6)。

\(\mathcal B\) 在 \(C_0(\mathbb R_\xi)\) 中一致稠密：对光滑紧支频率函数，
其逆Fourier变换是Schwartz函数；将逆变换光滑截断于越来越大的紧区间，在L¹收敛，
故Fourier变换一致收敛。再用光滑紧支频率函数在C₀中的一致稠密性即可。
令 \(\mathcal E=\overline{\mathcal D}^{\|\cdot\|}\)，则所有紧算子都在E内，且(6)给
\[
                   \mathcal E/\mathbb K(\mathcal H)
                              \cong C_0(\mathbb R_\xi).     \tag{7}
\]
这是本项目固定采样产生的实际C*商，不是只给抽象K群接口。
未在此求其完整K边界或把它与原源的几何主根空间识别。

## 3. 原正象限乘子在商上只剩标量

426的 \(\mathcal M_Q=\{c1+J:J=QJQ\in\mathcal B(\mathcal H)\}\) 满足
\(JA(h),A(h)J\in\mathcal S_1\)。因此
\[
 [RA(h)]=c[A(h)]=[A(h)R],\qquad R=c1+J.                    \tag{8}
\]
特别原提升 \(T=1+Q(u-1)Q\) 的左右商作用恒为单位。
所以仅用T的这项循环相容性无法限制商上的线性读出。
任意这些有界R还保持E的左右作用，因而是这个新C*代数E的实际双侧乘子；
它们是否属于原交叉积的乘子仍是另一类型问题，不在此混同。
原未压缩的酉元u不享有(8)的准入，见[429](429-f1-original-unitary-crosses-the-fixed-corner-domain.md)。

## 4. LF拓扑下的全部受限相容读出

使用426明确指定的拓扑：从 \(C_c^\infty(\mathbb R)\) 的LF拓扑与 \(\mathcal S_1\) 的迹范数
经 \((h,S)\mapsto A(h)+S\) 传递的商拓扑。由(4)此映射单射，所以它就是线性直和拓扑；
没有将这个拓扑替换成算子范数。

全部连续线性泛函 \(\Phi:\mathcal D\to\mathbb C\)，若在S₁上匹配普通迹，准确为
\[
                \Phi_\ell(A(h)+S)=\ell(h)+\operatorname{Tr}S,
                             \qquad\ell\in\mathcal D'(\mathbb R). \tag{9}
\]
证明是直和上的线性分解与 \((C_c^\infty)'=\mathcal D'\)：必要性取 \(\ell(h)=\Phi(A(h))\)，
充分性由该直和拓扑立即给出。
每一个(9)都满足426的全部 \(\mathcal M_Q\) 双模循环条件，因为
\([R,A(h)]\) 迹类且普通迹零，S₁部分也合法循环。
反过来，循环条件并没有进一步缩小(9)的分布自由度。

物理 \(\widetilde\Lambda\) 对应 \(\ell=\Lambda\)，\(\Psi_0\) 对应 \(\ell=0\)，只是全部选择中的两个。
这些读出在整个新代数上都具有427同一个交换子缺陷，均不是全代数标量迹。
这是完整的受限分类，不是凭两个反例推测无限自由度。

## 5. 算子商拓扑的要求更强

任何匹配全部S₁普通迹的读出都不可能在 \(\mathcal D\) 的算子范数上连续：
取秩n投影 \(P_n\)，则
\[
                     \|P_n/n\|=1/n\to0,
                    \qquad \Phi(P_n/n)=1.                 \tag{10}
\]
两个(9)的差消灭S₁，才可讨论其在算子商范数上的连续性。
由(6)–(7)及C₀的测度表示，它连续当且仅当存在有限复Radon测度μ使
\[
              (\ell_1-\ell_2)(h)=\int 2\widehat h(\xi)\,d\mu(\xi). \tag{11}
\]
这里μ是频率测度；LF分类中的任意时间分布一般没有这种有界表示。

原物理周期读出与零周期读出的差就不满足(11)。取
\(\eta\in C_c^\infty\)，\(\eta(0)=1\)，令
\[
 h_\varepsilon(s)=\eta((s+L)/\varepsilon).
\]
充分小的ε使支集避开0和其他两个轴的周期。由425的原有限部，
\[
 \Lambda(h_\varepsilon)=L\rho_p\ne0,\qquad
 \|A(h_\varepsilon)\|_{\rm ess}
      \le2\|h_\varepsilon\|_1=2\varepsilon\|\eta\|_1\to0.    \tag{12}
\]
这严格排除了物理周期读出在该符号范数上的连续性。
它不否定其在LF测试拓扑下的合法连续性，亦不否定原指定物理截止的比较。

## 6. 对后续Chern比较的实际约束

当前得到的是同源固定采样的精确符号、商范数和全受限读出分类。
单独要求普通迹匹配、原T循环、或算子商一致连续性，均不能完成原周期读出的规范选择：
前两者允许任意时间分布，最后一个甚至排除原周期原子。
427的非零商余圈提供必须携带的边界异常，但不选择 \(\ell\)。
需要把原物理球截止及真正源u的边／角链纳入扩大后的相对域，而非仅给同级迹公理。
实位、全素数Weil比较、有效性／RR及RH仍开放。
