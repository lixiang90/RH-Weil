# 实际 amplified mixed column：根节点独立全文审查

2026-10-07。限定 PASS：准入、exact transfer、列范数、spike 保留与现有
前向指数比较。没有认证新的 mixed power saving 或边界。

## 冻结对象与来源

全文从磁盘核读
[研究稿](hybrid-amplified-mixed-column-research.md)，canonical LF SHA-256：

~~~text
5f07dc2626ef0fa5ec20f0a56ab113b3ed55679ad066bb93174e1ee98d843752
~~~

20777 UTF-8 bytes、371 行。canonical 仅 CRLF、孤立 CR→LF，不 trim。
只读来源 math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a，
paper.tex canonical SHA
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
根节点另读原 12343–12475、9311–9314 与 4348 起的 deleted-product 段，
并对照上一轮 actual critical core 和冻结 450/451 的接口。
来源通用引理为 [R]，本审查不认证整个源证明或 kernel。

## 独立核算

1. **行与天然零。** 各 prime valuation modulo six 恢复 u，商恢复 a；
   primary generator 恢复单位。这只使 (u,a)→ua⁶ injective，并不需 gcd=1。
   ψ_(ua⁶)(n)=ψ_u(n)1_((n,a)=1) 恰保留所有新 natural zeros。
   primitive character、Θ 资格不变，presentation radical 增大仍须计费。

2. **三个列及 slots。** μ 列只取 rad(a) 的 squarefree d；每份 plain
   列却必须取全部 a-smooth h。按 n=hn' 唯一分解核得两个 q_h⁻¹/²
   与 q_d⁻¹/²，不能限 h squarefree。原 prime list 一次使用，
   p|a 的部分是外部 scalar R_i，不能作为新 fixed slot coefficient。
   (6) 不添加任何 pairwise coprimality；共享 a-primes 均由自然零处理。

3. **全部成本。** 有效 h 有限，local L¹ mass
   (1+q_p⁻¹/²)/(1−q_p⁻¹/²)² 以任意小 divisor loss 支付。
   tuple ℓ²=O(1)，merged fiber 按 d₃(N) 给 T_col^ε。
   好范数不改变 μ×1×1 的真实 length、independent annuli 或 column class。
   若 N=cb⁶，则 b 的 natural mask 与 radical 仍在，不能只保 c。

4. **放大和 spikes。** weighted Cauchy 后以 ≥cA 个 a 平均，再用行
   injectivity，正是 A⁻¹⁺ε、output width UA⁶ 和每个删除 slot 的 P_i⁻¹。
   scale supremum 在新 mixed raw moment 被证明之后才允许调用 Sobolev；
   研究稿没有免费使用它作为已知矩。固定 positive mesh 后
   R_i=o(1)，原 |Q_i|≥1 的 spike 保留。polynomial deleted products 与
   原有限高度 pointwise bounds 使大 q_d/q_h 尾不足以承担 saturated
   M/S，故近原 scale 的同时 spikes 也保留；这里没有新增 covariance。

5. **连续指数。** 令 UA⁶=U^η，实际 averaging 费用
   E(η)=(1+5η)/6。marked 两个 width 取
   max{1,ℓ+2z',(2ℓ+8z')/3}；其 retained-slot rate 在两个区间分别
   有导数 5/3−2q、20/9−2q，均严格正。plain width 为
   max{1,2m+6κ_act z'}，超过原 capacity 后导数 5κ_act−2q>0。
   因而这两个明确合同加 pointwise 的优化确实回到原两个 endpoints。
   这是限定的计算，不排除新的结构化 mixed 估计。

6. **未付阈值。** reference center 有 E(ℓ)−δℓ=R₀=2/3，
   故 amplified raw exponent η+γ 给 E(η)+γ；要低于
   1+δℓ，η↓ℓ 时必须 γ<1/3。原其他 pointwise 费用正好为 1/3，
   目前没有 strict χ。原泛化 dual β 是规定反射形态的 coefficient，
   不能直接接这个三列 polynomial。不同 Fourier heights 的三变量
   Mellin integral 也不会被裸 μ*1*1=1 取消。

## 结论范围

该稿实质新增合法的 whole mixed transfer、近原尺度同时 spike 保留和
具体 raw-toll 阈值。最重要的未付量是 actual structured raw moment
γ<1/3，包括 rowwise Γ profiles、不同 ν、原一次 Q_i、natural zeros
及有限高度阶。没有得到新零点比例、无零边界、全来源认证或 RH。
冻结正式论文不因此改写；Goal 继续 active。
