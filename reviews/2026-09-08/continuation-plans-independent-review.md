# 冻结续接方案、搜索实现及振幅支付复核

2026-09-08。Gibbs，01a0768d-8270-7400-a136-0e99610539be，只读。
**PASS，限于冻结214方案、8+24轮保存记录和高度／支付证书。**
全域势仍未证明。本报告不覆盖后来的backward实现。

1. Plans.value对任意m=1,...,4及偏置b准确实现357的V；
   即使缺少某一长度组，内部锚点成本仍累计。空方案为0。
   214方案×6状态的1284项逐锚点独立复算，最小值误差<=7.38e-18；
   缺少长度组及正负偏置另有检查，均只是双精度旁证。
2. extend正确取b+L(z,w1,w2,w3,w4)，再将prefix截为四gap。
   tail_ids在同批更新前计算，后续只追加，旧ID不变。
   31个负DE点生成的方案gap和偏置复算吻合，m=0,...,4恒等式均检查。
3. 两批8轮、24轮恢复顺序与去重正确；全部32轮96个DE点按
   plans[:plans_before_update]复算，样条残差完全复现，
   直接核残差最大差8.68e-19。未重跑DE或全部随机样本。
   最后一轮搜索用211方案，更新后才有214，不能把旧点当作最终候选的新搜索。
4. 精确小数冻结逐项对应源数据且SHA匹配。214含空方案；
   长度1、2、3、4数目49、86、32、46。全部gap在域内。
   pi<22/7给D<Dbar=36243171/8800000000。
   max(m Dbar-b)=124401796939229229/5500000000000000000<23/1000。
   最大项为ID10，m=4，b=-.006144339898041678。
   由解析定义，非紧域振幅也<.023。
5. H=.023，B=128，C=5alpha+H=2427/40000；
   eta B/(2pi)-C>894851/55000000>0，与证书全文一致。
   支付目标系数为alpha，不需额外5delta；内部delta属于势函数构造。

## 边界与采用建议

- 精确小数偏置定义新的固定候选；不证明之前浮点extend精确实现真实核更新。
  高度证明无需这种历史等价。
- 原resume只核alpha、eta，需核对profile哈希后才能跨版本继续。
  本次固定核版本通过；后续实现补充哈希检查。
- search_batches中的轮数是请求值，异常后以history为完成依据；
  本次完整8+24无歧义，后续实现补分请求和已完成计数。
- 非紧域高度定理不允许在样条域外调用默认浮点求值。
- B,H支付必须与另外证明的[5.7,128]^5势不等式结合；目前尚缺后者。

核读搜索脚本（含resume）、全部214冻结方案、32轮源历史、
高度脚本及输出全文；补核pi区间和356一般支付条款。
未调用写文件入口、修改文件、派生代理或核读backward脚本。

| 核读文件（说明修订前） | SHA-256 |
|---|---|
| radius_five_continuation_plan_search.py | b0a140397cb1d7fce42529bdbdaadc6c91dc1e853b36e85503409f214feaec0a |
| radius-five-continuation-plans-32.json | 3259bc5dd93b293511ea8d85d2047d0b3b3a30eb5a9a883e85c8d8104a735655 |
| continuation_plan_height_certificate.py | 317ba68b0d858f659303ecb8bc679a5374033a3da640270192bc92ceef05e865 |
| continuation-plan-height-certificate.json | 3d8327745e9d0f98bdacfdf21e94d0f53d66485865d1f41f833d018f621d9632 |
| radius-five-continuation-plan-search.json | 621c5c7775ba2b225e0ca3c5bba9d9cacb0bb8bc4463ccef9aa5d26d71d400ff |
| periodic_window_quadratic_certificate.py | 7366f1a002d51eb599fb2a7802f6db8a5d1a995e5a01224017b818254cc2a735 |
| radius-five-rational-profile-candidate.json | 3a89799a5705cc8c30c629643f32d72ee000c34bf67798510d6bfdd8575bdca0 |
| 356 | 2621ec930b13aef55a28691a342ec0365575479d6773c4aa983edcbf71edb114 |
