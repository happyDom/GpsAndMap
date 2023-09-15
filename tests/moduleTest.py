# -*- coding:UTF-8 -*-

# region 引入必要依赖
from src.GpsAndMap.MapModule import *

# endregion

地图 = 地图类().添加瓦片.智图GeoQ().地图

地图.添加基地(常用坐标.北京市)

地图.允许资源置换.保存html(目标路径='.').打开()
