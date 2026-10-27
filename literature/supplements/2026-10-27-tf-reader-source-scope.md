# 固定五源reader：来源、实际核读与缓存身份

2026-10-27。实际原对象依项目已消费的532/533实位Sonin投影／裸求值、535完整source trace、560全fixed窗桥和570源夹心／全returns；本轮核读这些原稿，没有重新宣称读完CCM／Burnol原论文，也未串新paper。准确版本／历史阅读仍保原库记录。

新增重核的外部来源限NIST DLMF两式：[5.7.6 digamma partial fractions](https://dlmf.nist.gov/5.7.E6)与[5.15.1 trigamma series](https://dlmf.nist.gov/5.15.E1)。root与源分支实际读官方HTML公式及其z≠0,−1,…的适用域；当前Re z=1/4合法。页脚观测Version1.2.8／release2026-09-15。全Γ界16+log(2+|s|)、导数10／36与节点尾是本项目从该式推导的粗界，不当DLMF原页直接给出的常数，未核全文所有证明。

直接下载两式TeX时代理GET返回HTTP403；web工具的TeX请求因MIME不支持也未取得原字节。HTML公式读取成功，故本地保存了标明身份的两条tool-visible normalized equation缓存，**不是原始作者TeX下载**。`reviews/2026-10-27/tf-reader/dlmf-source-read-record.json`记录URL、时间、缓存字节／SHA及失败状态。缓存位于忽略的 `literature/local/2026-10-27-tf-reader/`；Git仅保存元数据／阅读范围及本项目证明，不提交页面／公式缓存。

本轮自己的 `scripts/tf_reader_arch_gap_certificate.py` 及 `reviews/2026-10-27/tf-reader/arch-gap-certificate.json` 是实际运行的有理算术operator证明witness，不是外部文献或T/E数值实验。N20、160位向外区间、Machin交错π界、exact HHinv和两正LDL列表支付固定C0 gap／R0上界；独立fresh复算同数据。初次输出大有理字符串遇序列化限制后已以向外舍入短witness修复，最终证书有效。

建设性预检与全部未执行范围见[root总稿](../../goals/reviews/2026-10-27-five-source-actual-trace-reader-precheck.md)及[消费收据](../../reviews/2026-10-27/tf-reader/root-consumption-scope.json)。原du/Dlog、全Γ/contact、properpowers与双pole、Hilbert residual角色保留；尚无q0/T/E表或Hfin符号，不据来源／证书完成RH Goal。
