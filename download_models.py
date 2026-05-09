"""在 Windows 上预下载 CosyVoice 模型到本地。

用法:
    pip install modelscope
    python download_models.py

模型将下载到当前目录的 pretrained_models/ 下。
然后把 pretrained_models/ 整体拷贝到服务器上的 CosyVoice/ 目录即可。

服务器启动命令:
    python runtime/python/fastapi/server.py --port 5001 --model_dir pretrained_models/CosyVoice2-0.5B
"""

from modelscope import snapshot_download

# CosyVoice2-0.5B — 推荐，速度和质量平衡好
print("=" * 60)
print("下载 CosyVoice2-0.5B (推荐，约 2GB)...")
print("=" * 60)
snapshot_download(
    "iic/CosyVoice2-0.5B",
    local_dir="pretrained_models/CosyVoice2-0.5B",
)
print("✓ CosyVoice2-0.5B 下载完成\n")

# Fun-CosyVoice3-0.5B — 最新最好，质量最高
print("=" * 60)
print("下载 Fun-CosyVoice3-0.5B (最新最好，约 2GB)...")
print("=" * 60)
snapshot_download(
    "FunAudioLLM/Fun-CosyVoice3-0.5B-2512",
    local_dir="pretrained_models/Fun-CosyVoice3-0.5B",
)
print("✓ Fun-CosyVoice3-0.5B 下载完成\n")

# CosyVoice-300M-SFT — v1 预训练音色 (中文女/中文男/英文女/英文男/日语男/粤语女/韩语女)
print("=" * 60)
print("下载 CosyVoice-300M-SFT (v1 预训练音色，约 1.5GB)...")
print("=" * 60)
snapshot_download(
    "iic/CosyVoice-300M-SFT",
    local_dir="pretrained_models/CosyVoice-300M-SFT",
)
print("✓ CosyVoice-300M-SFT 下载完成\n")

print("=" * 60)
print("全部下载完成！")
print("")
print("模型位置: pretrained_models/")
print("  - CosyVoice-300M-SFT   (v1, 有预置音色: 中文女/中文男/英文女/英文男等)")
print("  - CosyVoice2-0.5B      (v2, 仅 zero_shot/instruct2, 需提供参考音频)")
print("  - Fun-CosyVoice3-0.5B  (v3 最新最好, 仅 zero_shot/instruct2, 需提供参考音频)")
print("")
print("将 pretrained_models/ 目录拷贝到服务器的 CosyVoice/ 下即可。")
print("")
print("服务器启动:")
print("  # v1 SFT (支持预置音色, 可直接用 spk_id='中文女' 等)")
print("  python runtime/python/fastapi/server.py --port 5001 --model_dir pretrained_models/CosyVoice-300M-SFT")
print("")
print("  # v2 (需提供参考音频, 用 zero_shot/instruct2 接口)")
print("  python runtime/python/fastapi/server.py --port 5001 --model_dir pretrained_models/CosyVoice2-0.5B")
print("=" * 60)
