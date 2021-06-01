
adb push frida-server-14.2.18-android-arm /data/local/tmp/frida-server
adb push frida-server-14.0.6-android-x86 /data/local/tmp/frida-server
adb shell
cd data/local/tmp
chmod 777 frida-server
./frida-server

//查看服务是否运行
frida-ps -U

问题1：Failed to spawn: timeout was reached
解决方案：
adb shell
setenforce 0
//验证
getenforce

# 方法1：导出前台应用dex
# 不确定是否需要代理转发 https://www.jianshu.com/p/43e4f3f7c434
frida -U -f com.zhlm.maotaiauthenticate -l dumpDex.js --no-pause
frida -U -f com.zhlm.maotaiauthenticate -l dexDump.js --no-pause
frida -U -f com.mt99dna.android -l dumpDex.js --no-pause
frida -U -f com.mt99dna.android -l dexDump.js --no-pause
frida -U -f com.youlu.fakao -l dexDump.js --no-pause


# 方法2：导出前台应用dex
frida-dexdump
