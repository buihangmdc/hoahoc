"""
Script: generate_autofit_pptx_bai1.py
Purpose: Generate PowerPoint presentation with dynamic auto-fit typography:
- Header Title: 34pt with dynamic auto-shrink (34pt -> 30pt -> 28pt) to prevent wrapping/collision.
- Card Title: 28pt with dynamic auto-shrink (28pt -> 24pt -> 22pt) to maintain clean 1-line display.
- Body Text / Bullets: 26pt (with auto-scaling to 24pt when fitting tight multi-line blocks).
- Guaranteed dynamic vertical separation: Content is ALWAYS offset below titles to prevent overlapping.
- Widescreen 16:9 (13.333" x 7.5"), rich visuals, transitions, on-click animations.
"""

import os
import sys
import io
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ==========================================
# PALETTE MÀU SẮC CHUẨN SƯ PHẠM CAO CẤP
# ==========================================
COLOR_NAVY_DARK = RGBColor(11, 37, 69)       # #0B2545 - Nền Header & Slide Bìa
COLOR_NAVY_LIGHT = RGBColor(19, 64, 116)     # #134074 - Khối phụ
COLOR_ROYAL_BLUE = RGBColor(37, 99, 235)     # #2563EB - Điểm nhấn Xanh dương
COLOR_SKY_BLUE = RGBColor(141, 169, 196)     # #8DA9C4 - Màu chữ phụ trên nền tối
COLOR_ICE_BG = RGBColor(245, 247, 250)       # #F5F7FA - Nền slide dịu mắt
COLOR_WHITE = RGBColor(255, 255, 255)        # #FFFFFF - Nền Card
COLOR_AMBER = RGBColor(245, 158, 11)         # #F59E0B - Điểm nhấn Vàng Cam
COLOR_AMBER_BG = RGBColor(254, 243, 199)     # #FEF3C7 - Nền Hộp Chú ý
COLOR_AMBER_BORDER = RGBColor(251, 191, 36)  # #FBBF24
COLOR_EMERALD = RGBColor(16, 185, 129)       # #10B981 - Màu Xanh Lá Chuẩn
COLOR_EMERALD_BG = RGBColor(209, 250, 229)   # #D1FAE5 - Nền Đáp án Đúng
COLOR_TEXT_MAIN = RGBColor(30, 41, 59)       # #1E293B - Màu chữ nội dung chính
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)   # #64748B - Màu chữ phụ
COLOR_CARD_BORDER = RGBColor(203, 213, 225)  # #CBD5E1 - Viền Card rõ nét
COLOR_RED_ACCENT = RGBColor(239, 68, 68)     # #EF4444 - Mâu thuẫn / Cảnh báo

ASSET_DIR = Path("dau-ra/bai-day/vat-ly-10/bai-1-khai-quat-ve-mon-vat-li/assets_img")

# -------------------------------------------------------------
# AUTO-FIT TYPOGRAPHY HELPER FUNCTIONS
# -------------------------------------------------------------

def calculate_title_font_size(text, max_width_inches, base_size=34):
    """
    Tính toán cỡ chữ tự động cho Tiêu đề Slide để nằm trọn trên 1 dòng.
    Ước lượng độ rộng: 1 ký tự chữ hoa chiếm khoảng 0.55 * fontSize (pt).
    """
    length = len(text)
    # Khoảng ký tự ước tính tối đa cho chiều rộng
    # width_in_pt = max_width_inches * 72
    avail_pt = max_width_inches * 72
    char_width_factor = 0.52
    
    req_pt = length * (base_size * char_width_factor)
    if req_pt <= avail_pt:
        return base_size
    
    # Scale down incrementally
    for test_size in [32, 30, 28, 26, 24]:
        if length * (test_size * char_width_factor) <= avail_pt:
            return test_size
    return 24

def calculate_card_title_font_size(text, max_width_inches, base_size=28):
    """
    Tính toán cỡ chữ tự động cho Tiêu đề Card để không bị tràn dòng.
    """
    length = len(text)
    avail_pt = max_width_inches * 72
    char_width_factor = 0.54
    
    req_pt = length * (base_size * char_width_factor)
    if req_pt <= avail_pt:
        return base_size
    
    for test_size in [26, 24, 22, 20]:
        if length * (test_size * char_width_factor) <= avail_pt:
            return test_size
    return 20

def add_slide_transition(slide, trans_type="fade"):
    """Thêm hiệu ứng chuyển slide (Fade/Push)"""
    trans_xml = parse_xml(f'<p:transition {nsdecls("p")} spd="med"><p:{trans_type}/></p:transition>')
    slide._element.append(trans_xml)

def add_click_animations(slide, shape_ids):
    """Gán hiệu ứng xuất hiện tuần tự (Fade In) theo từng lượt Click của Giáo viên"""
    if not shape_ids:
        return
    child_nodes = []
    bld_nodes = []
    c_tn_id = 3
    for sp_id in shape_ids:
        c_tn_id_set = c_tn_id + 2
        c_tn_id_anim = c_tn_id + 3
        child_xml = f'''
        <p:par {nsdecls("p")}>
          <p:cTn id="{c_tn_id}" fill="hold">
            <p:stCondLst><p:cond delay="0"/></p:stCondLst>
            <p:childTnLst>
              <p:par>
                <p:cTn id="{c_tn_id + 1}" fill="hold">
                  <p:stCondLst><p:cond delay="0"/></p:stCondLst>
                  <p:childTnLst>
                    <p:set>
                      <p:cBhvr>
                        <p:cTn id="{c_tn_id_set}" dur="1" fill="hold"/>
                        <p:tgtEl><p:spTgt spid="{sp_id}"/></p:tgtEl>
                        <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>
                      </p:cBhvr>
                      <p:to><p:strVal val="visible"/></p:to>
                    </p:set>
                    <p:animEffect transition="in" filter="fade">
                      <p:cBhvr>
                        <p:cTn id="{c_tn_id_anim}" dur="350"/>
                        <p:tgtEl><p:spTgt spid="{sp_id}"/></p:tgtEl>
                      </p:cBhvr>
                    </p:animEffect>
                  </p:childTnLst>
                </p:cTn>
              </p:par>
            </p:childTnLst>
          </p:cTn>
        </p:par>
        '''
        child_nodes.append(child_xml)
        bld_nodes.append(f'<p:bldP {nsdecls("p")} spid="{sp_id}" grpId="0" animBg="1"/>')
        c_tn_id += 4
    
    children_combined = "".join(child_nodes)
    blds_combined = "".join(bld_nodes)
    timing_xml = parse_xml(f'''
    <p:timing {nsdecls("p")}>
      <p:tnLst>
        <p:par>
          <p:cTn id="1" dur="indefinite" restart="always" nodeType="tmRoot">
            <p:childTnLst>
              <p:seq concurrent="1" nextAc="seek">
                <p:cTn id="2" dur="indefinite" nodeType="mainSeq">
                  <p:childTnLst>
                    {children_combined}
                  </p:childTnLst>
                </p:cTn>
                <p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>
                <p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>
              </p:seq>
            </p:childTnLst>
          </p:cTn>
        </p:par>
      </p:tnLst>
      <p:bldLst>{blds_combined}</p:bldLst>
    </p:timing>
    ''')
    slide._element.append(timing_xml)

def set_slide_background(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def create_header(slide, activity_badge, main_title):
    """Tạo Header chuẩn với Tiêu đề Auto-fit 34pt"""
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.35))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = COLOR_NAVY_DARK
    top_bar.line.color.rgb = COLOR_NAVY_DARK
    
    accent_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.35), Inches(13.333), Inches(0.06))
    accent_line.fill.solid()
    accent_line.fill.fore_color.rgb = COLOR_AMBER
    accent_line.line.color.rgb = COLOR_AMBER

    if activity_badge:
        badge_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.38), Inches(2.7), Inches(0.58))
        badge_box.fill.solid()
        badge_box.fill.fore_color.rgb = COLOR_NAVY_LIGHT
        badge_box.line.color.rgb = COLOR_AMBER
        badge_box.line.width = Pt(2)
        tf = badge_box.text_frame
        p = tf.paragraphs[0]
        p.text = activity_badge.upper()
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_AMBER
        p.font.name = 'Segoe UI'
        p.alignment = PP_ALIGN.CENTER
    
    title_left = Inches(0.6) if not activity_badge else Inches(3.5)
    title_width_in = 12.1 if not activity_badge else 9.3
    
    # Auto-fit title font size
    fitted_title_size = calculate_title_font_size(main_title, title_width_in, base_size=34)
    
    title_box = slide.shapes.add_textbox(title_left, Inches(0.2), Inches(title_width_in), Inches(0.95))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = main_title
    p_title.font.size = Pt(fitted_title_size)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE
    p_title.font.name = 'Segoe UI'

    # Footer
    footer_box = slide.shapes.add_textbox(Inches(0.6), Inches(7.1), Inches(12.133), Inches(0.35))
    tf_foot = footer_box.text_frame
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = "VẬT LÍ 10 — BÀI 1: NHẬP MÔN HÓA HỌC | KẾT NỐI TRI THỨC VỚI CUỘC SỐNG"
    p_foot.font.size = Pt(11)
    p_foot.font.color.rgb = COLOR_TEXT_MUTED
    p_foot.font.name = 'Segoe UI'

def add_card_with_autofit(slide, left, top, width, height, title="", bg_color=COLOR_WHITE, border_color=COLOR_CARD_BORDER, base_title_size=28):
    """
    Tạo Card với Tiêu đề tự động co chữ (Auto-fit) và trả về:
    (card_shape, content_start_top, title_font_size)
    để đảm bảo khối nội dung bên dưới LUÔN cách tiêu đề một khoảng an toàn, không bao giờ bị đè!
    """
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(2.0)
    
    content_start_top = top + Inches(0.2)
    
    if title:
        width_in = width.inches - 0.4
        fitted_size = calculate_card_title_font_size(title, width_in, base_size=base_title_size)
        
        # Chiều cao hộp tiêu đề ước tính
        title_box_height = Inches(0.6)
        title_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.12), Inches(width_in), title_box_height)
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(fitted_size)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY_DARK
        p.font.name = 'Segoe UI'
        
        content_start_top = top + Inches(0.72)
    
    return card, content_start_top

def add_bullet_list(slide, left, top, width, height, items, font_size=26, text_color=COLOR_TEXT_MAIN, space_after=8):
    """Thêm danh sách nội dung với cỡ chữ chuẩn 26pt - 28pt"""
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(font_size)
        p.font.color.rgb = text_color
        p.font.name = 'Segoe UI'
        p.space_after = Pt(space_after)
    return box

def safe_add_image(slide, img_name, left, top, width, height, border_color=COLOR_CARD_BORDER):
    """Chèn hình ảnh với khung viền thẩm mỹ"""
    img_path = ASSET_DIR / img_name
    if img_path.exists():
        frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        frame.fill.solid()
        frame.fill.fore_color.rgb = COLOR_WHITE
        frame.line.color.rgb = border_color
        frame.line.width = Pt(2.0)
        pad = Inches(0.06)
        pic = slide.shapes.add_picture(str(img_path), left + pad, top + pad, width - pad*2, height - pad*2)
        return frame, pic
    return None, None

def generate_master_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================
    # SLIDE 1: BÌA BÀI GIẢNG (TITLE SLIDE)
    # =========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_NAVY_DARK)
    add_slide_transition(s1, "fade")

    main_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(11.733), Inches(6.3))
    main_card.fill.solid()
    main_card.fill.fore_color.rgb = RGBColor(15, 23, 42)
    main_card.line.color.rgb = COLOR_AMBER
    main_card.line.width = Pt(3.0)

    tag_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.5), Inches(0.9), Inches(8.333), Inches(0.55))
    tag_box.fill.solid()
    tag_box.fill.fore_color.rgb = COLOR_NAVY_LIGHT
    tag_box.line.color.rgb = COLOR_ROYAL_BLUE
    tf_tag = tag_box.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = "VẬT LÍ 10 — KẾT NỐI TRI THỨC VỚI CUỘC SỐNG"
    p_tag.font.size = Pt(18)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_AMBER
    p_tag.alignment = PP_ALIGN.CENTER

    title_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(1.8))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p1 = tf_title.paragraphs[0]
    p1.text = "BÀI 1: NHẬP MÔN HÓA HỌC"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.alignment = PP_ALIGN.CENTER
    p1.font.name = 'Segoe UI'

    p2 = tf_title.add_paragraph()
    p2.text = "Thời lượng: 01 tiết (45 phút)  •  Chuẩn Công văn 5512"
    p2.font.size = Pt(24)
    p2.font.color.rgb = COLOR_SKY_BLUE
    p2.alignment = PP_ALIGN.CENTER
    p2.font.name = 'Segoe UI'

    div_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.0), Inches(3.55), Inches(5.333), Inches(0.06))
    div_bar.fill.solid()
    div_bar.fill.fore_color.rgb = COLOR_AMBER
    div_bar.line.color.rgb = COLOR_AMBER

    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(3.85), Inches(5.3), Inches(2.2))
    b1.fill.solid()
    b1.fill.fore_color.rgb = COLOR_NAVY_DARK
    b1.line.color.rgb = COLOR_ROYAL_BLUE
    b1.line.width = Pt(2.0)
    tf_b1 = b1.text_frame
    tf_b1.word_wrap = True
    p_b1_title = tf_b1.paragraphs[0]
    p_b1_title.text = "🎯 MỤC TIÊU TRỌNG TÂM"
    p_b1_title.font.size = Pt(22)
    p_b1_title.font.bold = True
    p_b1_title.font.color.rgb = COLOR_AMBER
    for it in [
        "Đối tượng & Vai trò Hóa học",
        "2 Phương pháp nghiên cứu cốt lõi"
    ]:
        p = tf_b1.add_paragraph()
        p.text = f"• {it}"
        p.font.size = Pt(20)
        p.font.color.rgb = COLOR_WHITE

    b2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.833), Inches(3.85), Inches(5.3), Inches(2.2))
    b2.fill.solid()
    b2.fill.fore_color.rgb = COLOR_NAVY_DARK
    b2.line.color.rgb = COLOR_EMERALD
    b2.line.width = Pt(2.0)
    tf_b2 = b2.text_frame
    tf_b2.word_wrap = True
    p_b2_title = tf_b2.paragraphs[0]
    p_b2_title.text = "⚡ ĐỔI MỚI NĂNG LỰC SỐ"
    p_b2_title.font.size = Pt(22)
    p_b2_title.font.bold = True
    p_b2_title.font.color.rgb = COLOR_EMERALD
    for it in [
        "Thiết kế Infographic (NLS 4.1.3)",
        "Trải nghiệm AI Prompting (AI-V10)"
    ]:
        p = tf_b2.add_paragraph()
        p.text = f"• {it}"
        p.font.size = Pt(20)
        p.font.color.rgb = COLOR_WHITE

    bot_box = s1.shapes.add_textbox(Inches(1.0), Inches(6.2), Inches(11.333), Inches(0.45))
    tf_bot = bot_box.text_frame
    p_bot = tf_bot.paragraphs[0]
    p_bot.text = "Giáo viên: Nhóm Chuyên môn Hóa học  •  Năm học: 2026 - 2027"
    p_bot.font.size = Pt(16)
    p_bot.font.italic = True
    p_bot.font.color.rgb = COLOR_SKY_BLUE
    p_bot.alignment = PP_ALIGN.CENTER

    add_click_animations(s1, [b1.shape_id, b2.shape_id])

    # =========================================================
    # SLIDE 2: MỤC TIÊU BÀI HỌC
    # =========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLOR_ICE_BG)
    add_slide_transition(s2, "push")
    create_header(s2, "YCCĐ", "MỤC TIÊU BÀI HỌC CẦN ĐẠT")

    c1, top1 = add_card_with_autofit(s2, Inches(0.6), Inches(1.6), Inches(5.9), Inches(5.3), "1. KIẾN THỨC CỐT LÕI", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=28)
    add_bullet_list(s2, Inches(0.8), top1 + Inches(0.1), Inches(5.5), Inches(4.3), [
        "Nắm rõ đối tượng: Vận động của VẬT CHẤT & NĂNG LƯỢNG.",
        "Phân tích vai trò của Hóa học qua 4 cuộc Cách mạng công nghiệp.",
        "Trình bày quy trình 2 phương pháp: Thực nghiệm & Lí thuyết."
    ], font_size=26, space_after=14)

    c2, top2 = add_card_with_autofit(s2, Inches(6.8), Inches(1.6), Inches(5.9), Inches(5.3), "2. NĂNG LỰC ĐẶC THÙ & SỐ", COLOR_WHITE, COLOR_EMERALD, base_title_size=28)
    add_bullet_list(s2, Inches(7.0), top2 + Inches(0.1), Inches(5.5), Inches(4.3), [
        "Tìm hiểu tự nhiên: Phân tích thí nghiệm rơi tự do chuẩn xác.",
        "NLS 4.1.3: Thiết kế Infographic số tóm tắt lịch sử phát minh.",
        "AI-V10: Thực hành câu lệnh Prompt đối thoại cùng nhà bác học."
    ], font_size=26, space_after=14)

    add_click_animations(s2, [c1.shape_id, c2.shape_id])

    # =========================================================
    # SLIDE 3: HOẠT ĐỘNG 1: KHỞI ĐỘNG (THÍ NGHIỆM SỰ RƠI)
    # =========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, COLOR_ICE_BG)
    add_slide_transition(s3, "push")
    create_header(s3, "HĐ 1 (5p)", "KHỞI ĐỘNG: BÍ ẨN SỰ RƠI CỦA CÁC VẬT")

    c_tn1, top_tn1 = add_card_with_autofit(s3, Inches(0.6), Inches(1.6), Inches(5.9), Inches(3.6), "TN 1: GIẤY PHẲNG & SỎI", COLOR_WHITE, COLOR_RED_ACCENT, base_title_size=28)
    safe_add_image(s3, "slide_058_shape_06.png", Inches(4.2), top_tn1 + Inches(0.05), Inches(2.1), Inches(2.6))
    add_bullet_list(s3, Inches(0.8), top_tn1 + Inches(0.05), Inches(3.3), Inches(2.6), [
        "Thả tờ giấy phẳng & viên sỏi cùng lúc.",
        "Kết quả: Sỏi rơi nhanh chạm đất trước, giấy rơi chậm."
    ], font_size=26, space_after=10)

    c_tn2, top_tn2 = add_card_with_autofit(s3, Inches(6.8), Inches(1.6), Inches(5.9), Inches(3.6), "TN 2: GIẤY VO TRÒN & SỎI", COLOR_WHITE, COLOR_EMERALD, base_title_size=28)
    safe_add_image(s3, "slide_059_shape_03.png", Inches(10.4), top_tn2 + Inches(0.05), Inches(2.1), Inches(2.6))
    add_bullet_list(s3, Inches(7.0), top_tn2 + Inches(0.05), Inches(3.3), Inches(2.6), [
        "Vo tròn tờ giấy rồi thả cùng viên sỏi.",
        "Kết quả: Cả hai chạm đất CÙNG MỘT LÚC!"
    ], font_size=26, space_after=10)

    c_conflict, top_conf = add_card_with_autofit(s3, Inches(0.6), Inches(5.4), Inches(12.1), Inches(1.55), "❓ MÂU THUẪN NHẬN THỨC", COLOR_AMBER_BG, COLOR_AMBER_BORDER, base_title_size=28)
    add_bullet_list(s3, Inches(0.8), top_conf + Inches(0.05), Inches(11.7), Inches(0.8), [
        "Vì sao cùng khối lượng, vo tròn lại rơi nhanh hơn? Quan niệm Aristotle có đúng?"
    ], font_size=28, text_color=COLOR_NAVY_DARK)

    add_click_animations(s3, [c_tn1.shape_id, c_tn2.shape_id, c_conflict.shape_id])

    # =========================================================
    # SLIDE 4: ARISTOTLE VS GALILEO GALILEI
    # =========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, COLOR_ICE_BG)
    add_slide_transition(s4, "push")
    create_header(s4, "Lịch sử", "BƯỚC NGOẶT: ARISTOTLE VS GALILEI")

    card_ari, top_ari = add_card_with_autofit(s4, Inches(0.6), Inches(1.6), Inches(5.9), Inches(4.3), "ARISTOTLE (350 TCN)", COLOR_WHITE, COLOR_NAVY_LIGHT, base_title_size=28)
    safe_add_image(s4, "slide_058_shape_07.png", Inches(0.8), top_ari + Inches(0.05), Inches(2.1), Inches(3.3))
    add_bullet_list(s4, Inches(3.0), top_ari + Inches(0.05), Inches(3.3), Inches(3.3), [
        "Quan sát cảm tính đời thường.",
        "Khẳng định: 'Vật nặng luôn rơi nhanh hơn vật nhẹ!'"
    ], font_size=26, space_after=12)

    card_gali, top_gali = add_card_with_autofit(s4, Inches(6.8), Inches(1.6), Inches(5.9), Inches(4.3), "GALILEO GALILEI (TK XVII)", COLOR_WHITE, COLOR_EMERALD, base_title_size=28)
    safe_add_image(s4, "slide_059_shape_02.png", Inches(7.0), top_gali + Inches(0.05), Inches(2.1), Inches(3.3))
    add_bullet_list(s4, Inches(9.2), top_gali + Inches(0.05), Inches(3.3), Inches(3.3), [
        "Thực nghiệm Tháp nghiêng Pisa.",
        "Chân lí: Không có sức cản không khí, MỌI VẬT RƠI NHƯ NHAU!"
    ], font_size=26, space_after=12)

    bot_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(6.05), Inches(12.1), Inches(0.95))
    bot_card.fill.solid()
    bot_card.fill.fore_color.rgb = COLOR_NAVY_DARK
    bot_card.line.color.rgb = COLOR_AMBER
    bot_card.line.width = Pt(2.0)
    tf_take = bot_card.text_frame
    p_t = tf_take.paragraphs[0]
    p_t.text = "💡 BÀI HỌC: Thực nghiệm khoa học là thước đo chân lí tối cao!"
    p_t.font.size = Pt(28)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_AMBER
    p_t.alignment = PP_ALIGN.CENTER

    add_click_animations(s4, [card_ari.shape_id, card_gali.shape_id, bot_card.shape_id])

    # =========================================================
    # SLIDE 5: ĐỐI TƯỢNG NGHIÊN CỨU CỦA HÓA HỌC
    # =========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, COLOR_ICE_BG)
    add_slide_transition(s5, "push")
    create_header(s5, "HĐ 2.1 (7p)", "ĐỐI TƯỢNG NGHIÊN CỨU CỦA HÓA HỌC")

    card_mat, top_mat = add_card_with_autofit(s5, Inches(0.6), Inches(1.6), Inches(5.9), Inches(5.3), "1. THẾ GIỚI VẬT CHẤT", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=28)
    safe_add_image(s5, "slide_005_shape_02.jpg", Inches(0.8), top_mat + Inches(0.05), Inches(2.6), Inches(2.1))
    safe_add_image(s5, "slide_007_shape_02.jpg", Inches(3.6), top_mat + Inches(0.05), Inches(2.7), Inches(2.1))
    add_bullet_list(s5, Inches(0.8), top_mat + Inches(2.3), Inches(5.5), Inches(2.1), [
        "Dạng CHẤT: Hạt sơ cấp, nguyên tử, phân tử, vật thể.",
        "Dạng TRƯỜNG: Trường hấp dẫn, điện từ trường."
    ], font_size=26, space_after=10)

    card_nrg, top_nrg = add_card_with_autofit(s5, Inches(6.8), Inches(1.6), Inches(5.9), Inches(5.3), "2. CÁC DẠNG NĂNG LƯỢNG", COLOR_WHITE, COLOR_EMERALD, base_title_size=28)
    safe_add_image(s5, "slide_024_shape_02.jpg", Inches(7.0), top_nrg + Inches(0.05), Inches(2.6), Inches(2.1))
    safe_add_image(s5, "slide_010_shape_01.png", Inches(9.8), top_nrg + Inches(0.05), Inches(2.7), Inches(2.1))
    add_bullet_list(s5, Inches(7.0), top_nrg + Inches(2.3), Inches(5.5), Inches(2.1), [
        "Cơ năng, Nhiệt năng, Điện năng, Quang năng.",
        "Hệ thức Einstein: E = m · c² (c ≈ 3·10⁸ m/s)."
    ], font_size=26, space_after=10)

    add_click_animations(s5, [card_mat.shape_id, card_nrg.shape_id])

    # =========================================================
    # SLIDE 6: CÁC CẤP ĐỘ PHẠM VI NGHIÊN CỨU
    # =========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, COLOR_ICE_BG)
    add_slide_transition(s6, "push")
    create_header(s6, "Phạm vi", "CÁC CẤP ĐỘ PHẠM VI NGHIÊN CỨU")

    c_micro, top_mic = add_card_with_autofit(s6, Inches(0.6), Inches(1.6), Inches(3.8), Inches(5.3), "1. VI MÔ (Micro)", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=26)
    safe_add_image(s6, "slide_006_shape_01.jpg", Inches(0.8), top_mic + Inches(0.05), Inches(3.4), Inches(2.3))
    add_bullet_list(s6, Inches(0.8), top_mic + Inches(2.45), Inches(3.4), Inches(2.0), [
        "Kích thước: 10⁻¹⁸ m ➔ 10⁻⁹ m.",
        "Hạt sơ cấp, electron, nguyên tử."
    ], font_size=24, space_after=8)

    c_macro, top_mac = add_card_with_autofit(s6, Inches(4.75), Inches(1.6), Inches(3.8), Inches(5.3), "2. VĨ MÔ (Macro)", COLOR_WHITE, COLOR_EMERALD, base_title_size=26)
    safe_add_image(s6, "slide_025_shape_08.jpg", Inches(4.95), top_mac + Inches(0.05), Inches(3.4), Inches(2.3))
    add_bullet_list(s6, Inches(4.95), top_mac + Inches(2.45), Inches(3.4), Inches(2.0), [
        "Kích thước: 10⁻⁶ m ➔ 10⁷ m.",
        "Vật thể đời sống, Trái Đất."
    ], font_size=24, space_after=8)

    c_cosmic, top_cos = add_card_with_autofit(s6, Inches(8.9), Inches(1.6), Inches(3.8), Inches(5.3), "3. SIÊU VĨ MÔ", COLOR_WHITE, COLOR_AMBER_BORDER, base_title_size=26)
    safe_add_image(s6, "slide_004_shape_01.jpg", Inches(9.1), top_cos + Inches(0.05), Inches(3.4), Inches(2.3))
    add_bullet_list(s6, Inches(9.1), top_cos + Inches(2.45), Inches(3.4), Inches(2.0), [
        "Kích thước: > 10⁹ m.",
        "Hệ Mặt Trời, Thiên hà, Vũ trụ."
    ], font_size=24, space_after=8)

    add_click_animations(s6, [c_micro.shape_id, c_macro.shape_id, c_cosmic.shape_id])

    # =========================================================
    # SLIDE 7: MỤC TIÊU MÔN HÓA HỌC Ở TRƯỜNG THPT
    # =========================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, COLOR_ICE_BG)
    add_slide_transition(s7, "push")
    create_header(s7, "Mục tiêu", "MỤC TIÊU MÔN HÓA HỌC Ở TRƯỜNG THPT")

    c_left, top_l7 = add_card_with_autofit(s7, Inches(0.6), Inches(1.6), Inches(6.8), Inches(5.3), "3 TRỤ CỘT MỤC TIÊU CHÍNH", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=28)
    add_bullet_list(s7, Inches(0.8), top_l7 + Inches(0.1), Inches(6.4), Inches(4.3), [
        "1. Hình thành Thế giới quan khoa học & nhận thức đúng bản chất tự nhiên.",
        "2. Phát triển Năng lực tìm hiểu tự nhiên & kĩ năng thực nghiệm sáng tạo.",
        "3. Định hướng nghề nghiệp trong kỉ nguyên Công nghệ số & Trí tuệ nhân tạo (AI)."
    ], font_size=26, space_after=14)

    c_right, top_r7 = add_card_with_autofit(s7, Inches(7.7), Inches(1.6), Inches(5.0), Inches(5.3), "ỨNG DỤNG THỰC TIỄN", COLOR_WHITE, COLOR_EMERALD, base_title_size=28)
    safe_add_image(s7, "slide_025_shape_10.jpg", Inches(7.9), top_r7 + Inches(0.05), Inches(4.6), Inches(2.0))
    safe_add_image(s7, "slide_025_shape_09.jpg", Inches(7.9), top_r7 + Inches(2.25), Inches(4.6), Inches(2.1))

    add_click_animations(s7, [c_left.shape_id, c_right.shape_id])

    # =========================================================
    # SLIDE 8: TIẾN TRÌNH LỊCH SỬ PHÁT TRIỂN
    # =========================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, COLOR_ICE_BG)
    add_slide_transition(s8, "push")
    create_header(s8, "HĐ 2.2 (10p)", "LỊCH SỬ PHÁT TRIỂN VẬT LÍ HỌC")

    t1, top_t1 = add_card_with_autofit(s8, Inches(0.6), Inches(1.6), Inches(3.8), Inches(5.3), "1. TIỀN VẬT LÍ", COLOR_WHITE, COLOR_NAVY_LIGHT, base_title_size=26)
    safe_add_image(s8, "slide_058_shape_07.png", Inches(0.8), top_t1 + Inches(0.05), Inches(3.4), Inches(2.0))
    add_bullet_list(s8, Inches(0.8), top_t1 + Inches(2.15), Inches(3.4), Inches(2.3), [
        "350 TCN ➔ Thế kỉ XVI.",
        "Aristotle, Archimedes.",
        "Quan sát cảm tính."
    ], font_size=24, space_after=8)

    t2, top_t2 = add_card_with_autofit(s8, Inches(4.75), Inches(1.6), Inches(3.8), Inches(5.3), "2. CỔ ĐIỂN", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=26)
    safe_add_image(s8, "slide_059_shape_02.png", Inches(4.95), top_t2 + Inches(0.05), Inches(3.4), Inches(2.0))
    add_bullet_list(s8, Inches(4.95), top_t2 + Inches(2.15), Inches(3.4), Inches(2.3), [
        "TK XVII ➔ Cuối TK XIX.",
        "Galilei, Newton, Maxwell.",
        "Phương pháp Thực nghiệm."
    ], font_size=24, space_after=8)

    t3, top_t3 = add_card_with_autofit(s8, Inches(8.9), Inches(1.6), Inches(3.8), Inches(5.3), "3. HIỆN ĐẠI", COLOR_WHITE, COLOR_EMERALD, base_title_size=26)
    safe_add_image(s8, "slide_024_shape_01.png", Inches(9.1), top_t3 + Inches(0.05), Inches(3.4), Inches(2.0))
    add_bullet_list(s8, Inches(9.1), top_t3 + Inches(2.15), Inches(3.4), Inches(2.3), [
        "Đầu TK XX ➔ Nay.",
        "Planck, Einstein, Bohr.",
        "Lượng tử & Tương đối."
    ], font_size=24, space_after=8)

    add_click_animations(s8, [t1.shape_id, t2.shape_id, t3.shape_id])

    # =========================================================
    # SLIDE 9: HAI PHƯƠNG PHÁP NGHIÊN CỨU & MÔ HÌNH HÓA
    # =========================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, COLOR_ICE_BG)
    add_slide_transition(s9, "push")
    create_header(s9, "Phương pháp", "HAI PHƯƠNG PHÁP NGHIÊN CỨU VẬT LÍ")

    # 1. Phương pháp thực nghiệm (Auto-fit title 24pt to stay strictly 1 line)
    c_exp, top_exp = add_card_with_autofit(s9, Inches(0.6), Inches(1.6), Inches(5.9), Inches(4.3), "1. PHƯƠNG PHÁP THỰC NGHIỆM", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=24)
    add_bullet_list(s9, Inches(0.8), top_exp + Inches(0.05), Inches(5.5), Inches(3.4), [
        "1. Xác định vấn đề nghiên cứu.",
        "2. Quan sát & Thu thập thông tin.",
        "3. Đưa ra dự đoán (Giả thuyết).",
        "4. Làm Thí nghiệm kiểm tra.",
        "5. Phân tích & Rút ra Kết luận."
    ], font_size=26, space_after=6)

    # 2. Phương pháp mô hình (Auto-fit title 24pt)
    c_theo, top_theo = add_card_with_autofit(s9, Inches(6.8), Inches(1.6), Inches(5.9), Inches(4.3), "2. PHƯƠNG PHÁP MÔ HÌNH", COLOR_WHITE, COLOR_EMERALD, base_title_size=24)
    safe_add_image(s9, "slide_061_shape_07.jpg", Inches(7.0), top_theo + Inches(0.05), Inches(1.8), Inches(1.8))
    safe_add_image(s9, "slide_063_shape_05.png", Inches(9.0), top_theo + Inches(0.05), Inches(3.5), Inches(1.8))
    add_bullet_list(s9, Inches(7.0), top_theo + Inches(1.95), Inches(5.5), Inches(1.5), [
        "Mô hình vật chất: Quả địa cầu.",
        "Mô hình lí thuyết: Chất điểm ô tô.",
        "Mô hình toán học: Vectơ lực, phương trình."
    ], font_size=24, space_after=4)

    c_rel = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(6.05), Inches(12.1), Inches(0.95))
    c_rel.fill.solid()
    c_rel.fill.fore_color.rgb = COLOR_AMBER_BG
    c_rel.line.color.rgb = COLOR_AMBER_BORDER
    c_rel.line.width = Pt(2.0)
    tf_rel = c_rel.text_frame
    p_rel = tf_rel.paragraphs[0]
    p_rel.text = "⚡ Lí thuyết định hướng — Thực nghiệm là thước đo chân lí tối cao!"
    p_rel.font.size = Pt(28)
    p_rel.font.bold = True
    p_rel.font.color.rgb = COLOR_NAVY_DARK
    p_rel.alignment = PP_ALIGN.CENTER

    add_click_animations(s9, [c_exp.shape_id, c_theo.shape_id, c_rel.shape_id])

    # =========================================================
    # SLIDE 10: VẬT LÍ VỚI CMCN 1.0 & 2.0
    # =========================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, COLOR_ICE_BG)
    add_slide_transition(s10, "push")
    create_header(s10, "HĐ 2.3 (8p)", "VẬT LÍ VỚI CMCN 1.0 & 2.0")

    # Titles auto-fitted to 24pt so they fit strictly on 1 line
    c_rev1, top_r1 = add_card_with_autofit(s10, Inches(0.6), Inches(1.6), Inches(5.9), Inches(5.3), "CMCN 1.0: CƠ GIỚI HÓA (TK XVIII)", COLOR_WHITE, COLOR_NAVY_LIGHT, base_title_size=24)
    safe_add_image(s10, "slide_037_shape_02.jpg", Inches(0.8), top_r1 + Inches(0.05), Inches(2.6), Inches(2.1))
    safe_add_image(s10, "slide_039_shape_02.jpg", Inches(3.6), top_r1 + Inches(0.05), Inches(2.7), Inches(2.1))
    add_bullet_list(s10, Inches(0.8), top_r1 + Inches(2.3), Inches(5.5), Inches(2.1), [
        "Nhiệt học & Động cơ hơi nước James Watt.",
        "Cơ giới hóa sản xuất, tàu hỏa ra đời."
    ], font_size=26, space_after=10)

    c_rev2, top_r2 = add_card_with_autofit(s10, Inches(6.8), Inches(1.6), Inches(5.9), Inches(5.3), "CMCN 2.0: ĐIỆN KHÍ HÓA (TK XIX)", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=24)
    safe_add_image(s10, "slide_041_shape_02.png", Inches(7.0), top_r2 + Inches(0.05), Inches(2.6), Inches(2.1))
    safe_add_image(s10, "slide_045_shape_00.jpg", Inches(9.8), top_r2 + Inches(0.05), Inches(2.7), Inches(2.1))
    add_bullet_list(s10, Inches(7.0), top_r2 + Inches(2.3), Inches(5.5), Inches(2.1), [
        "Điện từ học & Máy phát điện, động cơ điện.",
        "Chiếu sáng đô thị, sản xuất dây chuyền."
    ], font_size=26, space_after=10)

    add_click_animations(s10, [c_rev1.shape_id, c_rev2.shape_id])

    # =========================================================
    # SLIDE 11: VẬT LÍ VỚI CMCN 3.0 & 4.0
    # =========================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, COLOR_ICE_BG)
    add_slide_transition(s11, "push")
    create_header(s11, "Kỉ nguyên Số", "VẬT LÍ VỚI CMCN 3.0 & 4.0")

    # Titles auto-fitted to 24pt
    c_rev3, top_r3 = add_card_with_autofit(s11, Inches(0.6), Inches(1.6), Inches(5.9), Inches(5.3), "CMCN 3.0: TỰ ĐỘNG HÓA (TK XX)", COLOR_WHITE, COLOR_EMERALD, base_title_size=24)
    safe_add_image(s11, "slide_047_shape_04.jpg", Inches(0.8), top_r3 + Inches(0.05), Inches(2.6), Inches(2.1))
    safe_add_image(s11, "slide_050_shape_00.png", Inches(3.6), top_r3 + Inches(0.05), Inches(2.7), Inches(2.1))
    add_bullet_list(s11, Inches(0.8), top_r3 + Inches(2.3), Inches(5.5), Inches(2.1), [
        "Hóa học Bán dẫn & Bóng Transistor (1947).",
        "Máy tính điện tử, Vi mạch vi xử lý & Internet."
    ], font_size=26, space_after=10)

    c_rev4, top_r4 = add_card_with_autofit(s11, Inches(6.8), Inches(1.6), Inches(5.9), Inches(5.3), "CMCN 4.0: THÔNG MINH HÓA (TK XXI)", COLOR_WHITE, COLOR_AMBER_BORDER, base_title_size=24)
    safe_add_image(s11, "slide_052_shape_03.jpg", Inches(7.0), top_r4 + Inches(0.05), Inches(2.6), Inches(2.1))
    safe_add_image(s11, "slide_055_shape_03.jpg", Inches(9.8), top_r4 + Inches(0.05), Inches(2.7), Inches(2.1))
    add_bullet_list(s11, Inches(7.0), top_r4 + Inches(2.3), Inches(5.5), Inches(2.1), [
        "Hóa học Lượng tử & Công nghệ Nano.",
        "Trí tuệ nhân tạo (AI), Máy tính lượng tử."
    ], font_size=26, space_after=10)

    add_click_animations(s11, [c_rev3.shape_id, c_rev4.shape_id])

    # =========================================================
    # SLIDE 12: ỨNG DỤNG VẬT LÍ & BẢO VỆ MÔI TRƯỜNG
    # =========================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, COLOR_ICE_BG)
    add_slide_transition(s12, "push")
    create_header(s12, "Ứng dụng", "ỨNG DỤNG VẬT LÍ & BẢO VỆ MÔI TRƯỜNG")

    c_med, top_med = add_card_with_autofit(s12, Inches(0.6), Inches(1.6), Inches(3.8), Inches(5.3), "1. Y TẾ HIỆN ĐẠI", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=26)
    safe_add_image(s12, "slide_025_shape_09.jpg", Inches(0.8), top_med + Inches(0.05), Inches(3.4), Inches(2.2))
    add_bullet_list(s12, Inches(0.8), top_med + Inches(2.35), Inches(3.4), Inches(2.0), [
        "Máy chụp MRI, CT-Scan.",
        "Laser phẫu thuật mắt."
    ], font_size=24, space_after=8)

    c_green, top_grn = add_card_with_autofit(s12, Inches(4.75), Inches(1.6), Inches(3.8), Inches(5.3), "2. NĂNG LƯỢNG XANH", COLOR_WHITE, COLOR_EMERALD, base_title_size=26)
    safe_add_image(s12, "slide_025_shape_08.jpg", Inches(4.95), top_grn + Inches(0.05), Inches(3.4), Inches(2.2))
    add_bullet_list(s12, Inches(4.95), top_grn + Inches(2.35), Inches(3.4), Inches(2.0), [
        "Pin mặt trời quang điện.",
        "Tuabin gió, Nhiệt hạch."
    ], font_size=24, space_after=8)

    c_eco, top_eco = add_card_with_autofit(s12, Inches(8.9), Inches(1.6), Inches(3.8), Inches(5.3), "3. MÔI TRƯỜNG", COLOR_WHITE, COLOR_AMBER_BORDER, base_title_size=26)
    safe_add_image(s12, "slide_122_shape_02.png", Inches(9.1), top_eco + Inches(0.05), Inches(3.4), Inches(2.2))
    add_bullet_list(s12, Inches(9.1), top_eco + Inches(2.35), Inches(3.4), Inches(2.0), [
        "Giảm phát thải CO2.",
        "Xử lý rác thải điện tử."
    ], font_size=24, space_after=8)

    add_click_animations(s12, [c_med.shape_id, c_green.shape_id, c_eco.shape_id])

    # =========================================================
    # SLIDE 13: LUYỆN TẬP: TRẮC NGHIỆM TƯƠNG TÁC (TÍNH TOÁN KHOẢNG CÁCH CHUẨN XÁC)
    # =========================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13, COLOR_ICE_BG)
    add_slide_transition(s13, "push")
    create_header(s13, "HĐ 3 (10p)", "LUYỆN TẬP: TRẮC NGHIỆM CỦNG CỐ")

    # Question 1
    q1 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.5), Inches(12.133), Inches(1.7))
    q1.fill.solid()
    q1.fill.fore_color.rgb = COLOR_WHITE
    q1.line.color.rgb = COLOR_ROYAL_BLUE
    q1.line.width = Pt(2.0)
    tf_q1 = q1.text_frame
    p_q1 = tf_q1.paragraphs[0]
    p_q1.text = "CÂU 1: Đối tượng nghiên cứu chủ yếu của môn Hóa học là gì?"
    p_q1.font.size = Pt(24)
    p_q1.font.bold = True
    p_q1.font.color.rgb = COLOR_NAVY_DARK

    opt1_a = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.35), Inches(5.8), Inches(0.7))
    opt1_a.fill.solid()
    opt1_a.fill.fore_color.rgb = COLOR_EMERALD_BG
    opt1_a.line.color.rgb = COLOR_EMERALD
    opt1_a.line.width = Pt(2.5)
    opt1_a.text = " A. Vật chất và Năng lượng. [ĐÚNG ✔]"
    opt1_a.text_frame.paragraphs[0].font.size = Pt(22)
    opt1_a.text_frame.paragraphs[0].font.bold = True
    opt1_a.text_frame.paragraphs[0].font.color.rgb = COLOR_NAVY_DARK
    
    opt1_b = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.35), Inches(5.7), Inches(0.7))
    opt1_b.fill.solid()
    opt1_b.fill.fore_color.rgb = COLOR_WHITE
    opt1_b.line.color.rgb = COLOR_CARD_BORDER
    opt1_b.text = " B. Sự biến đổi chất hóa học."
    opt1_b.text_frame.paragraphs[0].font.size = Pt(22)
    opt1_b.text_frame.paragraphs[0].font.color.rgb = COLOR_TEXT_MAIN

    # Question 2
    q2 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(3.35), Inches(12.133), Inches(1.7))
    q2.fill.solid()
    q2.fill.fore_color.rgb = COLOR_WHITE
    q2.line.color.rgb = COLOR_ROYAL_BLUE
    q2.line.width = Pt(2.0)
    tf_q2 = q2.text_frame
    p_q2 = tf_q2.paragraphs[0]
    p_q2.text = "CÂU 2: Nhà bác học mở đầu Phương pháp Thực nghiệm khoa học là:"
    p_q2.font.size = Pt(24)
    p_q2.font.bold = True
    p_q2.font.color.rgb = COLOR_NAVY_DARK

    opt2_a = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.2), Inches(5.8), Inches(0.7))
    opt2_a.fill.solid()
    opt2_a.fill.fore_color.rgb = COLOR_WHITE
    opt2_a.line.color.rgb = COLOR_CARD_BORDER
    opt2_a.text = " A. Aristotle."
    opt2_a.text_frame.paragraphs[0].font.size = Pt(22)
    opt2_a.text_frame.paragraphs[0].font.color.rgb = COLOR_TEXT_MAIN

    opt2_c = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.2), Inches(5.7), Inches(0.7))
    opt2_c.fill.solid()
    opt2_c.fill.fore_color.rgb = COLOR_EMERALD_BG
    opt2_c.line.color.rgb = COLOR_EMERALD
    opt2_c.line.width = Pt(2.5)
    opt2_c.text = " C. Galileo Galilei. [ĐÚNG ✔]"
    opt2_c.text_frame.paragraphs[0].font.size = Pt(22)
    opt2_c.text_frame.paragraphs[0].font.bold = True
    opt2_c.text_frame.paragraphs[0].font.color.rgb = COLOR_NAVY_DARK

    # Question 3
    q3 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.2), Inches(12.133), Inches(1.7))
    q3.fill.solid()
    q3.fill.fore_color.rgb = COLOR_WHITE
    q3.line.color.rgb = COLOR_ROYAL_BLUE
    q3.line.width = Pt(2.0)
    tf_q3 = q3.text_frame
    p_q3 = tf_q3.paragraphs[0]
    p_q3.text = "CÂU 3: Phát minh là nền tảng khởi đầu của cuộc Cách mạng công nghiệp lần 3 (3.0):"
    p_q3.font.size = Pt(24)
    p_q3.font.bold = True
    p_q3.font.color.rgb = COLOR_NAVY_DARK

    opt3_b = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.05), Inches(5.8), Inches(0.7))
    opt3_b.fill.solid()
    opt3_b.fill.fore_color.rgb = COLOR_EMERALD_BG
    opt3_b.line.color.rgb = COLOR_EMERALD
    opt3_b.line.width = Pt(2.5)
    opt3_b.text = " B. Bóng bán dẫn (Transistor). [ĐÚNG ✔]"
    opt3_b.text_frame.paragraphs[0].font.size = Pt(22)
    opt3_b.text_frame.paragraphs[0].font.bold = True
    opt3_b.text_frame.paragraphs[0].font.color.rgb = COLOR_NAVY_DARK

    opt3_a = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(6.05), Inches(5.7), Inches(0.7))
    opt3_a.fill.solid()
    opt3_a.fill.fore_color.rgb = COLOR_WHITE
    opt3_a.line.color.rgb = COLOR_CARD_BORDER
    opt3_a.text = " A. Động cơ hơi nước."
    opt3_a.text_frame.paragraphs[0].font.size = Pt(22)
    opt3_a.text_frame.paragraphs[0].font.color.rgb = COLOR_TEXT_MAIN

    add_click_animations(s13, [opt1_a.shape_id, opt2_c.shape_id, opt3_b.shape_id])

    # =========================================================
    # SLIDE 14: VẬN DỤNG & NHIỆM VỤ SỐ TỰ HỌC
    # =========================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14, COLOR_ICE_BG)
    add_slide_transition(s14, "push")
    create_header(s14, "HĐ 4 (5p)", "VẬN DỤNG & NHIỆM VỤ SỐ TỰ HỌC")

    # Titles auto-fitted to 24pt
    c_t1, top_t14 = add_card_with_autofit(s14, Inches(0.6), Inches(1.6), Inches(5.9), Inches(5.3), "1. THIẾT KẾ SỐ (NLS 4.1.3)", COLOR_WHITE, COLOR_ROYAL_BLUE, base_title_size=24)
    safe_add_image(s14, "slide_025_shape_07.png", Inches(0.8), top_t14 + Inches(0.05), Inches(1.8), Inches(1.8))
    add_bullet_list(s14, Inches(2.8), top_t14 + Inches(0.05), Inches(3.5), Inches(4.3), [
        "Thiết kế 01 Infographic A4 trên Canva / XMind.",
        "Tóm tắt 4 cuộc Cách mạng công nghiệp gắn với phát minh Hóa học.",
        "Nộp file ảnh lên link Padlet lớp."
    ], font_size=26, space_after=12)

    c_t2, top_t24 = add_card_with_autofit(s14, Inches(6.8), Inches(1.6), Inches(5.9), Inches(5.3), "2. HƯỚNG NGHIỆP AI (AI-V10)", COLOR_WHITE, COLOR_EMERALD, base_title_size=24)
    safe_add_image(s14, "slide_053_shape_03.jpg", Inches(7.0), top_t24 + Inches(0.05), Inches(1.8), Inches(1.8))
    add_bullet_list(s14, Inches(9.0), top_t24 + Inches(0.05), Inches(3.5), Inches(4.3), [
        "Dùng AI với Prompt tra cứu 3 ngành nghề tương lai kết hợp Hóa học & AI.",
        "Viết thu hoạch 250 từ định hướng nghề nghiệp bản thân."
    ], font_size=26, space_after=12)

    add_click_animations(s14, [c_t1.shape_id, c_t2.shape_id])

    # =========================================================
    # SLIDE 15: TỔNG KẾT BÀI HỌC
    # =========================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15, COLOR_NAVY_DARK)
    add_slide_transition(s15, "fade")

    card_sum = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(11.733), Inches(6.3))
    card_sum.fill.solid()
    card_sum.fill.fore_color.rgb = RGBColor(15, 23, 42)
    card_sum.line.color.rgb = COLOR_AMBER
    card_sum.line.width = Pt(3.0)

    title_box_s15 = s15.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.333), Inches(0.8))
    tf_s15 = title_box_s15.text_frame
    p_s15 = tf_s15.paragraphs[0]
    p_s15.text = "TỔNG KẾT BÀI HỌC & ĐIỀU HƯỚNG"
    p_s15.font.size = Pt(34)
    p_s15.font.bold = True
    p_s15.font.color.rgb = COLOR_AMBER
    p_s15.alignment = PP_ALIGN.CENTER
    p_s15.font.name = 'Segoe UI'

    keywords = [
        ("VẬT CHẤT & NĂNG LƯỢNG", "Đối tượng nghiên cứu xuyên suốt mọi cấp độ."),
        ("PHƯƠNG PHÁP THỰC NGHIỆM", "Thước đo chân lí tối cao của khoa học."),
        ("NỀN TẢNG CÔNG NGHỆ", "Gốc rễ của 4 cuộc CMCN, Bán dẫn & AI."),
        ("TƯ DUY KHOA HỌC", "Trung thực, tôn trọng sự thật & bảo vệ môi trường.")
    ]
    for idx, (kw_title, kw_desc) in enumerate(keywords):
        x = Inches(1.2 + (idx % 2) * 5.6)
        y = Inches(1.9 + (idx // 2) * 1.8)
        kw_box = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.3), Inches(1.55))
        kw_box.fill.solid()
        kw_box.fill.fore_color.rgb = COLOR_NAVY_DARK
        kw_box.line.color.rgb = COLOR_ROYAL_BLUE
        kw_box.line.width = Pt(2.0)
        tf_kw = kw_box.text_frame
        tf_kw.word_wrap = True
        p_t = tf_kw.paragraphs[0]
        p_t.text = f"🔑 {kw_title}"
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_AMBER
        p_d = tf_kw.add_paragraph()
        p_d.text = kw_desc
        p_d.font.size = Pt(20)
        p_d.font.color.rgb = COLOR_WHITE

    next_box = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(5.5), Inches(10.9), Inches(1.1))
    next_box.fill.solid()
    next_box.fill.fore_color.rgb = COLOR_NAVY_LIGHT
    next_box.line.color.rgb = COLOR_EMERALD
    next_box.line.width = Pt(2.0)
    tf_next = next_box.text_frame
    p_n1 = tf_next.paragraphs[0]
    p_n1.text = "📖 ĐỌC TRƯỚC BÀI 2: CÁC QUY TẮC AN TOÀN TRONG PHÒNG THỰC HÀNH VẬT LÍ"
    p_n1.font.size = Pt(22)
    p_n1.font.bold = True
    p_n1.font.color.rgb = COLOR_EMERALD
    p_n1.alignment = PP_ALIGN.CENTER

    output_dir = Path("dau-ra/bai-day/hoa-hoc-10/bai-1-nhap-mon-hoa-hoc")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_pptx = output_dir / "Slide-PowerPoint-Bai-1-Hoa-hoc-10.pptx"
    prs.save(str(output_pptx))
    Path("dau-ra/giao-an").mkdir(parents=True, exist_ok=True)
    prs.save("dau-ra/giao-an/BAI_GIANG_BAI_1_HOA_HOC_10_TICH_HOP_AI.pptx")
    print(f"[SUCCESS] Đã lưu bài giảng PowerPoint Hóa học: {output_pptx}")

if __name__ == "__main__":
    generate_master_pptx()
