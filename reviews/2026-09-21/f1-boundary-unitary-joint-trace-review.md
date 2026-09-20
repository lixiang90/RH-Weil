# 414 独立joint-trace审查

2026-09-21。审查者读取可用临时副本，随后与原工作区同步对账；以下为完整原文，[原始返回](f1-boundary-unitary-joint-trace-review.raw.json)另存。临时副本依赖SHA与Git行尾有关，最终记录另核数学文本一致性。

**审查结论：§7–7.3、公式 (16)–(24) 通过；未发现 P0–P2 数学问题。存在两处 P3 记号风险。** 联合迹的成立不解决主消失，也不能据此认定完整 F1 几何已经构造完成。

审查范围为[稿件第156–258行](C:/Users/A/AppData/Local/Temp/rh-weil-414-recovery/414-recovery-draft.md:156)，对照指定 412 来源。前文仅提取本范围依赖的定义，未重复审核 §1–6。全程只读、未访问 H、未写文件、未运行 Git/Lean。

**逐项核查**

1. **共同壳层、秩与强极限：(16)–(18) 正确。**
   412 的 \(R_N\) 递增且秩为 \(2N+1\)，故 \(S_N=R_{N+1}-R_N\) 是秩二正交投影。非零迭代的压缩迹与 \(N\) 无关，作差恰得 (16)。\(E_pE_q=0\)，张量迹给出 (18) 的全部四种情形；单位元处
   \[
   \tfrac12\operatorname{rank}\Pi=2(N_p+N_q+1).
   \]
   两个截断参数均趋于无穷时，\(S_N\) 和 \(\Pi\) 强趋零成立；非零轴向迹保持不变不构成矛盾，因为此处没有迹范数收敛。

2. **原 A 的协变方向与真实时间：(19) 正确。**
   412 给 \(V_a e_j=e_{j-a}\)，因此稿件表示满足
   \[
   (\pi(U_p^aU_q^b)\psi)_{j,k}(t)
   =\psi_{j-a,k-b}(t-aL-bM).
   \]
   从而共轭乘法算子得到
   \(f(j-a,k-b,t-aL-bM)\)，正是原点作用的逆拉回。横向负指数与时间正参数必须同时保留。额外的 \(U_s\) 实现 \(\beta_s\)，并与群酉元交换。

3. **J 本质性及整个表示忠实：论证成立。**
   换坐标 \(x=t-jL-kM\) 后，群作用只平移离散指标；\(J\) 成为 \(C_0(\mathbb R_x)\otimes\mathcal K(\ell^2\mathbb Z^2)\) 的标准忠实、非退化表示。若元素消灭 \(J\)，各 Fourier 系数在稠密开层上消失，连续性迫使其处处消失。这里 \(\Gamma=\mathbb Z^2\) 可和，故完整与约化交叉积一致，Fourier 系数唯一性适用。于是 \(\pi\) 忠实，并忠实延拓到乘子代数。建议在第194–195行补明这句可和性依据。

4. **固定截断下的几何衰减：(22) 正确。**
   环带—球矩阵元的指标条件和指数均正确，反方向由伴随得到。事实上，在给定正交基中可以明确取
   \[
   \|R_KV_aR_K\|_1
   \le (2K+1)^2\rho^{-2K}\rho^{|a|}.
   \]
   再利用 \(E_p,E_q\le R_{N_p+1,p}\otimes R_{N_q+1,q}\)，得到全部四块的双几何衰减。常数允许依赖截断，不能据此声称对 \(N\) 一致。

5. **时间迹范数对稠密长度一致，完整 \(\mathbb Z^2\) 求和绝对收敛。**
   按光滑紧支截止的解释，稿件的周期 Fourier 展开成立，所需混合导数涉及 \(h\) 至多四阶导数，其界与平移量 \(\ell\) 无关。

   还可用更直接的证明补强：约定
   \(\widehat h(\xi)=\int h(s)e^{-i\xi s}\,ds\)，则
   \[
   M_{c_r}U_\ell U(h)M_{c_s}
   =\frac1{2\pi}\int
   \widehat h(\xi)e^{-i\xi\ell}
   |c_re^{i\xi\cdot}\rangle\langle c_se^{i\xi\cdot}|\,d\xi,
   \]
   是迹范数 Bochner 积分，并有
   \[
   \|M_{c_r}U_\ell U(h)M_{c_s}\|_1
   \le\frac{\|\widehat h\|_{L^1}}{2\pi}
   \|c_r\|_2\|c_s\|_2.
   \]
   此界对所有实数 \(\ell\) 一致。结合横向估计，
   \[
   \sum_{a,b}\|C_N\pi(U_p^aU_q^b)U(h)C_N\|_1
   \le K_{N,h}\sum_a\rho_p^{|a|}\sum_b\rho_q^{|b|}<\infty.
   \]
   因而没有遗漏稠密混合长度，也不需要共同紧基本区间。

6. **交叉块与混合项：(23) 正确。**
   有限秩横向块允许循环求迹：
   \[
   \operatorname{Tr}(E_rWE_s)
   =\operatorname{Tr}(E_sE_rW)=0\quad(r\ne s).
   \]
   这是迹零，交叉块算子本身未必为零。两个对角块的时间迹分别为 \(Lh(-aL-bM)\)、\(Mh(-aL-bM)\)；再用 (16)，全部混合项在完整求和之后消失，得到 (23)。

7. **长度、单位扣项和 (24) 的系数均正确。**
   平方分割积分给出 \(\int c_p^2=L\)、\(\int c_q^2=M\)，所以轴项系数是基本长度 \(\log p,\log q\)，没有额外迭代次数因子。代入
   \(h(s)=e^{-s/2}k(-s)\) 后，
   \[
   \rho_p^{|a|}h(-aL)=
   \begin{cases}
   k(aL),&a>0,\\
   p^{-m}k(-mL),&a=-m<0.
   \end{cases}
   \]
   与 [412 式 (13c)](C:/Users/A/AppData/Local/Temp/rh-weil-414-recovery/RH-Weil/notes/412-f1-transverse-compression-and-periodic-traces.md:157) 完全一致。单位扣项必须保留 \(2N_r+1\)；只扣 \(2N_r\) 会留下额外的 \((L+M)k(0)\)。

**P3 问题及必要文字修订**

- **[第197行](C:/Users/A/AppData/Local/Temp/rh-weil-414-recovery/414-recovery-draft.md:197)：\(c_q\) 复用。** 前文此符号表示 \(c(t-M)\)，这里则重新选择 \(M\)-长度平方分割。原来的平移函数平方积分仍为 \(L\)，不能当作这里的函数。建议新函数改名 \(d_q\)，明确写出
  \[
  d_q\in C_c^\infty(\mathbb R),\quad d_q\ge0,\quad
  \sum_n d_q(t-nM)^2=1.
  \]
  “另取”的现有表述足以恢复正确含义，因此不构成公式错误。

- **[第254行](C:/Users/A/AppData/Local/Temp/rh-weil-414-recovery/414-recovery-draft.md:254)：有限位半迹与截断 \(N_r\) 易混淆。** 应将标量有限位写成 \(\mathcal N_r(k)\)，明确
  \(\mathcal L_r(k)=2\mathcal N_r(k)\)。记
  \[
  D_N=(2N_p+1)L+(2N_q+1)M,
  \]
  则对来源指定的 sharp 测试，准确约定为
  \[
  \boxed{\;
  \mathcal N_p(k)+\mathcal N_q(k)
  =\tfrac14\operatorname{Tr}A_N(h)-\tfrac12D_Nk(0).
  \;}
  \]
  (24) 本身无需改系数：其中壳层的 \(1/2\) 尚未包含有限位半迹所需的另一个 \(1/2\)。

第255–258行的范围限定应保留：截止形状不改变上述迹值，但可改变算子；同处一个忠实表示并不证明迹下降到相对 K 类、消去 \(T\) 的边界，或给出完整 F1 几何。主消失仍开放。

读取前后 SHA-256 一致：

- **414 稿件：** `C9A0C1A9A3D02DA586030BAF08C1EC315A8491FC31667DC73B6F188226F28A1E`
- **412 来源：** `C64FA6E55F447F975010A470BE651F20D75E62EDC3CC31BF692949FB465D3C27`
