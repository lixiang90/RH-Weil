# 357有限续接方案与初始扩展复核

2026-09-08。Gibbs，01a0768d-8270-7400-a136-0e99610539be，只读。
**PASS，限于§2–3及初始扩展的[E]范围。** 不认证全域h、振幅.01或迭代收敛。

## 数学与实现

1. m<=3时，L(s,z)+V_(w,b)(shift)=V_((z,w),b)(s)；
   m=4时新prefix=(z,w1,w2,w3)，新偏置为b+L(z,w1,w2,w3,w4)。
   是加号，空后方案对应((z),0)。闭合的是参数形式；
   一个固定有限集合未必对所有实数z的Bellman运算闭合。
2. m<=4使所有已支付首gap仍为原状态s_i>=a；由F>=0得L>=-D。
   因此一个冻结有限集合满足min(0,min(b-mD))<=h<=0且连续。
   更新过程中b没有已证统一下界；初始完整网格续接集的浮点振幅预算约.022654，
   不能直接沿用.01。这与后来选出的较小方案集的预算不是同一数值。
3. 初始扩展value的内部／跨界五条边、税项、-alpha-delta均准确，
   j<=i+1和前缀重复顺序正确。四步终端索引、edge//q及edge%q^4一致。
   搜索残差是L+delta+Delta h，没有漏减margin。
4. 只读重建全部10000终端值，逐项与JSON差0；14步停止复现。
   同种子300个不同状态用默认样条回代，最大差2.949029909160572e-17。
   三个保存点的头尾方案复现，直接90项双精度残差为
   -.0006459861874293644、-.0007474027725500377、-.0004436196666287458。
5. 三符号、四状态共480条非空方案与批量实现最大差2.17e-19；
   抽查m=0,...,4续接恒等式吻合。未运行DE，全部实现旁证仍属浮点。

## 采用修订

- “粗续接gap不足”改为“出现负残差候选，尚未严格认证失败”。
  只重算选中分支时，R_true=R_selected+e_head-e_tail，
  其中e_head,e_tail>=0，不能据此确定真实最小值残差的符号。
- 样本检查注释改为stored floating-point finite-graph values；
  exact=True仅指直接90项双精度求值，非精确算术。
- 初始扩展只实现网格续接，不实现§3实数更新；
  状态域[5.7,80]^4、样条[0,400]，第三DE盒首gap额外限制<=29.2。
- 更新可能重开该过渡本身或其他负过渡，不保证单点修复。

实际范围：357§2–3（29–82行），初始解析扩展脚本全文、输出全部终端值；
核构造、基础核及profile输入只作依赖核读。§1作上下文；
审查期间新增§4及实数方案搜索脚本不在此报告内。
未重审profile成本、插值或外部文献，未写文件、未派生代理。

| 核读文件（说明修改前） | SHA-256 |
|---|---|
| 357（交付前哈希；实际范围如上） | eba54e6a00ba56bde14740b1e5ede912dc6f512c1e57205eefa0bd117b72655f |
| radius_five_analytic_bellman_extension.py | 71a9b74961ff0d7e6035f23fbf61f34a85fe1e61abdf02410e0119d303f0dd2e |
| radius-five-analytic-bellman-extension.json | 402d04ff2109ba66f4c20d87a5bcbd14417477fef82d59afd0ccdf4d2dc9d316 |
| radius_five_subaction_grid.py | 331a2eb223b4f9efff79330fe3ac77c58c5a4ee383c3fb6c25ddbc0ecbc8beca |
| radius-five-subaction-grid.json | 89408b896b4f30e1fb228df8f4df18905783c14060e9049eebbed22c137c523a |
| radius-five-rational-profile-candidate.json | 3a89799a5705cc8c30c629643f32d72ee000c34bf67798510d6bfdd8575bdca0 |
| spectral_four_point_prefilter.py | 70d6bfbbea62fa565efe0511548a0546e7d47031a3a9a1a1f1c711586282b218 |
