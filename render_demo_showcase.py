#!/usr/bin/env python3
import os
import subprocess
import sys

demo_dir = "/root/waoowaoo/demo_assets"
font_file = "/usr/local/share/fonts/vbbs/BeVietnamPro-SemiBold.ttf"
if not os.path.exists(font_file):
    font_file = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

ass_path = os.path.join(demo_dir, "subtitles.ass")
clip1_path = os.path.join(demo_dir, "clip1.mp4")
clip2_path = os.path.join(demo_dir, "clip2.mp4")
clip3_path = os.path.join(demo_dir, "clip3.mp4")
final_output = "/root/waoowaoo/waoo_ai_cinematic_demo.mp4"

# 1. Create ASS Subtitles with professional styling
ass_content = f"""[Script Info]
Title: Waoo AI Film Showcase
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Subtitle,Be Vietnam Pro,52,&H00FFFFFF,&H000000FF,&H000B0B14,&H80000000,-1,0,0,0,100,100,0,0,1,3.5,2,2,100,100,90,1
Style: Badge,Be Vietnam Pro,28,&H0000E5FF,&H000000FF,&H0005070E,&H90000000,-1,0,0,0,100,100,1.5,0,1,2.0,1,7,80,80,60,1
Style: SceneTag,Be Vietnam Pro,26,&H00FFFFFF,&H000000FF,&H0005070E,&H90000000,0,0,0,0,100,100,1.0,0,1,2.0,1,7,80,80,100,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.30,0:00:05.80,Badge,,0,0,0,,{{\\fade(200,200)}}WAOO AI  |  INDUSTRIAL FILM FACTORY
Dialogue: 0,0:00:00.50,0:00:05.80,SceneTag,,0,0,0,,{{\\fade(200,200)}}SCENE 01: SCRIPT-TO-CANVAS DECOMPOSITION
Dialogue: 0,0:00:00.60,0:00:05.40,Subtitle,,0,0,0,,{{\\fade(150,150)}}Chào mừng bạn đến với nhà máy sản xuất video công nghiệp Waoo AI.

Dialogue: 0,0:00:05.90,0:00:11.80,Badge,,0,0,0,,{{\\fade(200,200)}}WAOO AI  |  INDUSTRIAL FILM FACTORY
Dialogue: 0,0:00:06.00,0:00:11.80,SceneTag,,0,0,0,,{{\\fade(200,200)}}SCENE 02: MULTI-REFERENCE CHARACTER LOCKING
Dialogue: 0,0:00:05.90,0:00:11.70,Subtitle,,0,0,0,,{{\\fade(150,150)}}Tự động phân tách kịch bản, khóa nhất quán nhân vật qua mọi góc máy...

Dialogue: 0,0:00:11.90,0:00:17.80,Badge,,0,0,0,,{{\\fade(200,200)}}WAOO AI  |  INDUSTRIAL FILM FACTORY
Dialogue: 0,0:00:12.00,0:00:17.80,SceneTag,,0,0,0,,{{\\fade(200,200)}}SCENE 03: VEO & HAILUO NEURAL RENDER ENGINE
Dialogue: 0,0:00:11.90,0:00:17.30,Subtitle,,0,0,0,,{{\\fade(150,150)}}...và kết xuất chuỗi phân cảnh hoàn chỉnh với độ chi tiết vượt trội.\\nKỷ nguyên điện ảnh AI — Biến mọi ý tưởng thành hiện thực!
"""

with open(ass_path, "w", encoding="utf-8") as f:
    f.write(ass_content)

print(f"1. Written ASS subtitles to {ass_path}")

# 2. Render 3 high-quality cinematic clips with smooth camera motions
def render_clip(img_path, output_clip, zoom_expr, pan_x_expr, pan_y_expr, duration=6.0):
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", img_path,
        "-t", str(duration),
        "-vf", (
            f"scale=1920:1080:force_original_aspect_ratio=increase,"
            f"scale={zoom_expr}:eval=frame,"
            f"crop=1920:1080:{pan_x_expr}:{pan_y_expr},"
            f"format=yuv420p"
        ),
        "-r", "60",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        output_clip
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error rendering clip:", res.stderr)
        sys.exit(1)
    print(f"Rendered: {output_clip}")

print("2. Rendering Scene 1 (Establishing Shot - Slow Dolly In & Drift)...")
render_clip(
    f"{demo_dir}/frame1.jpg",
    clip1_path,
    zoom_expr="w='1920*(1+0.12*t/6)':h='1080*(1+0.12*t/6)'",
    pan_x_expr="'(in_w-1920)*0.5 + 40*(t/6)'",
    pan_y_expr="'(in_h-1080)*0.5'",
    duration=6.2
)

print("3. Rendering Scene 2 (Character Consistency Close-up - Eye Focus Push In)...")
render_clip(
    f"{demo_dir}/frame2.jpg",
    clip2_path,
    zoom_expr="w='1920*(1+0.15*t/6)':h='1080*(1+0.15*t/6)'",
    pan_x_expr="'(in_w-1920)*0.5'",
    pan_y_expr="'(in_h-1080)*0.35'",
    duration=6.2
)

print("4. Rendering Scene 3 (Neural Climax - Warp Through Matrix)...")
render_clip(
    f"{demo_dir}/frame3.jpg",
    clip3_path,
    zoom_expr="w='1920*(1+0.22*t/6)':h='1080*(1+0.22*t/6)'",
    pan_x_expr="'(in_w-1920)*0.5'",
    pan_y_expr="'(in_h-1080)*0.5'",
    duration=6.2
)

# 3. Composite everything: Transitions (xfade) + Subtitles + Dual Audio Mix (Voice + BGM Ducking)
print("5. Compositing full film with xfade transitions, audio ducking, and typography...")
filter_complex = f"""
[0:v][1:v]xfade=transition=fadeblack:duration=0.5:offset=5.7[v01];
[v01][2:v]xfade=transition=fadeblack:duration=0.5:offset=11.4[v_merged];
[v_merged]ass={ass_path}[vout];

[3:a]volume=0.30,afade=t=in:ss=0:d=1.0,afade=t=out:st=16.5:d=1.3[bgm_base];
[4:a]volume=1.2[vox];
[bgm_base][vox]amix=inputs=2:duration=first:dropout_transition=2[aout]
"""

cmd_final = [
    "ffmpeg", "-y",
    "-i", clip1_path,
    "-i", clip2_path,
    "-i", clip3_path,
    "-i", f"{demo_dir}/bgm.wav",
    "-i", f"{demo_dir}/voiceover.mp3",
    "-filter_complex", filter_complex,
    "-map", "[vout]",
    "-map", "[aout]",
    "-t", "17.8",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "256k",
    final_output
]

res = subprocess.run(cmd_final, capture_output=True, text=True)
if res.returncode != 0:
    print("Final composite error:", res.stderr)
    sys.exit(1)

# Also copy to artifact directory for easy download/preview
artifact_copy = "/root/.gemini/antigravity-cli/brain/55c352e7-9847-4be6-a4b0-721619275586/waoo_ai_cinematic_demo.mp4"
subprocess.run(["cp", final_output, artifact_copy])

print(f"🎬 SUCCESS! Final video rendered to: {final_output}")
print(f"Artifact copy saved to: {artifact_copy}")
