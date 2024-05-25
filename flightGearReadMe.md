# 安装和运行flightgear的注意事项
+ 安装地址和方法见
+ https://www.flightgear.org/
+ https://www.flightgear.org.cn/topic-jiaocheng.html

## 会出现的问题
+ win10 安装出现鼠标和键盘不能用，解决方法：
+ https://www.cnblogs.com/bg-fly/p/17993135
+ https://www.bilibili.com/video/BV1aH4y1y7Hk

## 运行中的技巧
+ 快速起飞请用机型 Diamond DA 双引擎飞机，操作简单，稳定性好，马力大。默认的飞机操控对新人不友好
+ 因为目的不是人工控制飞机，而是验证控制算法，所以飞机起飞简单点,就4步，1. 自动启动。2.拉油门。3.去制动。4.按停止键，设定自动飞行。
+ 其余尽量研究python接口

## python控制接口
+ https://flightgear-python.readthedocs.io/en/latest/

## 一些对比
+ 研究无人机群，发现flightgear 优点、缺点就是
1. 相对比airSim,对无人机群支持不够，需要花大力气，对flightgear和multiplayer的系统进行二次搭框架，而且对传感器支持不足，所以暂时放弃
2. 相对于airSim,消耗的CPU和GPU资源少，对于少量机群和控制算法模拟消耗资源比较少。简单来说，100架次以上的同时模拟，airSim 搞不定。flightgear也应该搞不定，但是加钱和优化以后也许可以
3. YASI和JSBSIM也许才是大规模机群模拟的核心部分