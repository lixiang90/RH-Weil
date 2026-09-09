# 只读独立复核（2026-09-09）

审查者：只读子代理 Gibbs。以下为修改前审查记录；不是外部同行评审。
采纳记录：交换 degree/codegree；SectionExistence 改以正自交为前提并经 trace_identification 使用；补入抽象包真空模型和几何比较断点。后续构建验证覆盖最终版本。

**结论：当前10个`sorry`均可保留为真实的经典待形式化命题，未发现必须撤销的错误命题。** 审查期间新增的`weil_convergence`已纳入。需要修正／明确的是双次数命名和抽象存在性接口的解释；本次未编辑、未启动构建。

| 现有`sorry` | 数学判断与准确范围 |
|---|---|
| `mem_primeLocalization_iff` | **正确。** 单位子环由 \(1/p\) 生成，元素恰为 \(a/p^n\)。 |
| `exponentPresheaf_isSheaf` | **正确。** Specℤ开集拟紧，有限子覆盖使兼容截面的总支集仍有限。 |
| `exponent_stalk_at_prime` | **正确。** 使用的确实是邻域图的余极限stalk；目前只声称底层集合等价。 |
| `finiteLift_circleIntegrable` | **正确。** 半径恒正，有限零极点的对数奇性可积。 |
| `jensen_finite_lift` | **正确。** 整数幂与前置单项式的符号准确；极点处总定义值仅影响零测集。 |
| `finiteProfile_weakSecond` | **正确。** 光滑紧支撑测试函数消去边界项，右侧保留全部正负跳跃；不是错误的点态二阶导数。 |
| `jensen_one_add_and_sub` | **正确。** 两者平均均为 \(\max(0,-x)\)，包括 \(x=0\)。 |
| `newtonEquivalent_iff_hull` | **正确。** 有限凸包加闭正象限是闭凸集；严格正方向的信息可连续延伸到边界方向。空表示也处理一致。 |
| `weil_convergence` | **正确。** 卷积光滑紧支撑；素数项实际只有有限多个非零项；无穷处积分在零点附近有可去极限，在无穷远指数衰减。 |
| `weilCriterion` | **真实经典桥梁。** 换元后的算术式与所引原文一致，终点是mathlib实际RH。完整显式公式及测试空间匹配仍是该`sorry`承担的经典证明工作。 |

具体接口意见：

1. **[Weil.lean:23](/F:/codex-build/RH/RH-Weil/formal/F1/Analysis/Weil.lean:23)：积分正确，但degree／codegree与原文命名互换。**

   令原变量函数为 \(f(u)=F(\log u)\)。当前两矩分别是
   \[
   \int F(x)\,dx=\int f(u)\frac{du}{u},\qquad
   \int e^xF(x)\,dx=\int f(u)\,du.
   \]
   原文采用 \(\deg\Psi(\lambda)=\lambda\)，故实际**degree应对应第二项**，codegree对应第一项。

   最小修正：交换两个定义的名称／内容，或明确整个接口采用转置后的次数约定。两个矩同时为零不受影响，`weilCriterion`不会因此变成错误命题。

   其余归一化正确：反演因子是`exp (-x)`；卷积使用`dt`；无穷处原来的 \(du/u\) 换成`dx`，**不应再乘`exp x`**。自然数求和多出的0、1项因von Mangoldt值为零而消失。

2. **[Sheaf.lean:49](/F:/codex-build/RH/RH-Weil/formal/F1/Arithmetic/Sheaf.lean:49)：是真stalk，但完成层级须准确。**

   当前`Nonempty (... ≃ primeCone p.val)`没有给出：
   - 茎同构对germ的求值公式；
   - 加法及Frobenius相容；
   - 泛点stalk；
   - 加吸收元后的层或球形代数比较。

   因此文档应写“指数集合层及其闭点stalk等价的形式化蓝图”。这些缺项不使现有两个`sorry`错误，也无需本轮全部完成。

3. **[Existence.lean:43](/F:/codex-build/RH/RH-Weil/formal/F1/Geometry/Existence.lean:43)：条件推理正确，但目前绕过自交识别。**

   `nonpositive_of_existence`确实没有使用`trace_identification`，因为`SectionExistence`直接以`0 < weilSelf f`为前提。

   最小文档修正：明确当前证明只验证“有效代表＋双次数不变＋有效刚性”的逻辑矛盾，尚未使用交叉理论。若要在类型层面强制走过自交桥梁，把存在性前提改成
   ```lean
   0 < M.intersection (M.arithmeticDivisor f) (M.arithmeticDivisor f)
   ```
   再通过`trace_identification`应用它。

   `c ≠ 0`允许正倍数或负倍数，数学上没有漏符号；`E ≠ 0`也已正确保留。

4. **[BareExistenceProblem](/F:/codex-build/RH/RH-Weil/formal/F1/Geometry/Existence.lean:70)须明确是RH强度的抽象包，不是裸F₁框架存在性。**

   可以独立看出其与`WeilNonpositive`等价：反向取自由实向量空间
   \[
   \mathrm{Divisor}=\mathrm{TestFunction}\to_0\mathbb R,\qquad D_f=e_f,
   \]
   以两个矩定义线性次数，以
   \[
   \langle e_f,e_g\rangle=
   \begin{cases}\mathrm{weilSelf}(f),&f=g,\\0,&f\ne g\end{cases}
   \]
   定义双线性配对，再取`principal = ⊥`、`effective = {0}`。在`WeilNonpositive`下，`SectionExistence`的正值前提不可能成立，因而真空成立。正向正是现有条件定理。

   所以结合经典桥梁，这个抽象存在命题具有RH等价强度；上述模型完全不需要算术层或Newton平方。**这不否定独立证明存在性的价值，但明确了它不能单独认证实际F₁构造。**

   当前`Existence.lean`只导入Weil，尚无连接Sheaf／ReducedSquare的比较映射；`arithmeticDivisor`也未要求线性。文档应将这些列为真实几何研究断点，而非经典`sorry`已覆盖的内容。

`RationalCorrespondence.lean`没有`sorry`的结论目前只是参数点满足方程、整数图复合及预定义shadow上的等式；尚未形式化参数化同构、投影次数或双圆积分识别。现有模块注释没有越界，文档保持这个范围即可。

审查快照SHA256：

```text
Analysis/Weil.lean
f9fc2f38f1089d6f2c953fa117f69b6aa5812bcb8ab0c3e6aa5f672b911d3e24
Analysis/Jensen.lean
660d7a745bc88efa80153943207cfd8687191691129bdfcee51c2ab185134e99
Arithmetic/Sheaf.lean
6196818f111f938ff5a978e30986ed1fd7b7ffc3f12461acbedbfdb336b4375b
Arithmetic/PrimeLocalization.lean
8820f3f1ac9142ab1d7a6a025764f8c00840d4c00d100f6860df150dd2dd9872
Arithmetic/FiniteSupport.lean
33ab336dee414b2ba01ad44dd471b20fef2937aa0426bda5caa7585c7cf11515
Geometry/ReducedSquare.lean
e82658066e1938b8f374db6ca9b77e0d8d8ea96f4b7d40995e0279411b5f4316
Geometry/RationalCorrespondence.lean
b49c2acb826358c62fca055e80ad80f519da74e5ef5c0f7c736d88a217111cc9
Geometry/Existence.lean
08d4561c75b1c80aae1c3771a57fb84ea9d47b82caf2b9832b04ca911fd2de15
```
