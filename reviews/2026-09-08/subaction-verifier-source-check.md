# 全域势认证方法的固定来源回查

2026-09-08。用于357之后的连续域验证设计，不导入外部数字为项目定理。

- 重读已存[Tawan六页PDF](../../literature/candidates/2026-tawan-bellman-6731929-45149f6.pdf)
  第3–6页，并核读固定提交的
  [Bellman记录](https://github.com/tawanerguo-cn/zeta-simple-zeros/blob/45149f6d403059a71be73c5e3f884cee7cd62b20/BELLMAN_COBBOUNDARY_PROOF.md)。
  它用显式线性／核平方coboundary重分配六gap的正系数，
  再以一体压力筛选、区间范围和凸切线覆盖剩余盒。
  主线程本次查看C++验证器的Hessian构造、精确LDL及切线下界（约431–543行），
  只核读导数生成器开头的依赖接口；未重新生成表、编译验证器或运行64盒。
- 核读[ainta验证器设计](https://github.com/ainta/zeta-simple-zeros/blob/040c5e899e658aed7b56a2a87f501798fe10761d/docs/verifier.md)：
  以Arb构造闭核单元下界、向下浮点换算及范围最小值，再穷尽细分。
  该方法说明不验证本项目不同窗口和min方案势；当前没有导入其执行日志。

Tawan原文还将全域谱对偶与Bellman势列为未来方向。
因此347以后不能把这一一般方向作为本项目首次提出；
实际新数值或新结构仍须依据本项目独立输入及完整全域证书判断。

本轮保存8份固定原件（Tawan6份、ainta2份，含各自MIT许可），
没有新增PDF；详情及SHA见[获取记录](interval-verifier-source-acquisition.json)
和[literature manifest](../../literature/manifest.json)。
下载及源码片段核读不是对外部作者67.3192911473%主张的完整认证。
本机所查Strawberry编译器／MPFR路径不存在；未把外部机器路径写成当前环境事实。
