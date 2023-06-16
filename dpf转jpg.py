import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import fitz

def convert_pdf_to_jpg():
    # 打开选择文件对话框
    pdf_path = filedialog.askopenfilename(title="选择PDF文件", filetypes=[("PDF Files", "*.pdf")])
    
    if pdf_path:
        # 获取用户输入的宽度和高度
        width = int(width_entry.get())
        height = int(height_entry.get())
        
        try:
            # 打开PDF文件
            doc = fitz.open(pdf_path)
            
            # 获取第一页
            page = doc[0]
            
            # 将PDF页面转换为图像
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # 调整图像大小
            img = img.resize((width, height), Image.LANCZOS)
            
            # 保存为JPG文件
            jpg_path = filedialog.asksaveasfilename(title="保存为JPG文件", defaultextension=".jpg", filetypes=[("JPEG Files", "*.jpg")])
            
            if jpg_path:
                img.save(jpg_path)
                messagebox.showinfo("转换成功", "PDF转换为JPG成功！")
            else:
                messagebox.showwarning("保存失败", "未选择保存路径！")
        except Exception as e:
            messagebox.showerror("转换失败", str(e))
    else:
        messagebox.showwarning("选择失败", "未选择PDF文件！")

# 创建主窗口
window = tk.Tk()
window.title("PDF转JPG")
window.geometry("400x200")

# 创建标签和输入框
width_label = tk.Label(window, text="宽度：")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()

height_label = tk.Label(window, text="高度：")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# 创建按钮
convert_button = tk.Button(window, text="转换", command=convert_pdf_to_jpg)
convert_button.pack()

# 运行主循环
window.mainloop()









