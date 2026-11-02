# oyster-video-tool
Video frame extraction tool for oyster behavior analysis
一.
# 视频抽帧工具（Extract_frames.py）

把视频按固定时间间隔抽成图片，用于牡蛎开闭行为的标注和检测。

## 怎么跑

    pip install opencv-python
    python extract_frames.py

需要把待处理视频命名为 `input.mp4`，放在同一目录下。

## 结果

3 分钟、60fps 的视频，每 2 秒抽一张 → 输出 91 张 jpg（间隔 120 帧），
存放于 `frames/`，文件名为帧序号（000000.jpg、000119.jpg…）。

## 已知限制

- 视频必须命名为 input.mp4（还没做命令行参数）
- 不支持中文路径
