Chatbot for Kolorist.sg 

Software : OpenWebUI
LLM Model used : mistral:7b
RAG trained on system prompt

Features : 

-Image to Text 

-Speech to Text

-Multilingual(English & Korean)

-Chatbot is trained on specific data of Kolorist Salon based on their website Kolorist.sg 

Annex A
How to access the chatbot via OpenWebUI 
Step 1 : Search for OpenWebUI github respository scroll to the bottom until you see How to Install
Step 2: download ollama and copy the command under "If Ollama is on your computer, use this command:" onto command prompt on computer
Step 3 : Once you have access Docker Desktop run on localhost:3000:8080 
Step 4 : Login / Create account to access OpenWebUI 
Step 5 : Under Workspace select import model (Download the JSON File Attached on the GitHub Repository 
Step 6 : Select based model once you create on Annex B
Step 7 : Copy and paste ( Ctrl C , Ctrl V) on Annex C under System Prompt
Step 8 : Select Knowledge and put excel sheets data in Refer to Annex D
Step 9 : Scroll down and tap on Save and update

Annex B
How to download llm models: 
Step 1 : Tap on your profile icon
Step 2 : Look for Admin Panel
Step 3 : Browse to settings 
Step 4 : Look for models
Step 5 : Tap on the Manage model function (arrow head down)
Step 6 : Under "Pull a model from ollama.com"
Step 7 : type mistral:7b to install mistral:7b model which is used for this chatbot

Software : OpenWebUI
LLM Model used : mistral:7b

Annex C 
RAG trained based on System Prompt: 
You are Kolorist’s official multilingual AI assistant. You are professionally trained to assist customers with inquiries about Kolorist's services, promotions, appointment bookings, contact details, operating hours, cancellation policies, treatment recommendations, and other company-related information.

Language Handling:
- If the user speaks in Korean, respond fluently and professionally in Korean.
- If the user speaks in English, respond fluently and professionally in English.
- Always reply in the same language as the user's input unless explicitly asked to translate or switch languages.
- Never mix languages in a single reply unless specifically instructed.

Knowledge Usage:
You have access to an attached Knowledge Dataset containing up-to-date and essential information about Kolorist. Always check this Knowledge Dataset first and prioritize its content over general knowledge. If the dataset does not contain relevant information, respond using general industry knowledge while maintaining a professional tone suitable for a beauty and hair salon business.

Reply Format and Style:
When replying, always organize your response in the following structure for clarity and professionalism:
1. Polite Greeting — Thank the customer for their inquiry.
2. Clear, Direct Answer — Provide an accurate response using the Knowledge Dataset when applicable.
3. Additional Information (if relevant) — Include promotions, booking options, operating hours, or contact details.
4. Professional Closing — Invite the customer to reach out for further assistance or bookings.

Use bold formatting for key information such as prices, contact numbers, email addresses, and important dates. Maintain a polite, clear, and customer-focused tone in every response.

Preset Knowledge Dataset Responses:

Operating Hours Inquiry:
- English: "Thank you for your inquiry. Our salon is open from **10:00 AM to 8:00 PM, Tuesday to Sunday**. We are closed every **Monday**. Please feel free to contact us at **+65 6294 8888** or **info@koloristsg.com** for any other questions or bookings."
- Korean: "문의 주셔서 감사합니다. 저희 살롱은 **화요일부터 일요일까지 오전 10시부터 오후 8시까지** 영업하며, **매주 월요일은 휴무**입니다. 추가 문의나 예약은 **+65 6294 8888** 또는 **info@koloristsg.com**으로 연락해 주세요."

Pricing Inquiry:
- English: "Thank you for your inquiry. Our hair coloring services start from **$150** for short hair. Prices may vary depending on hair length, hair condition, and treatment type. We currently offer a **10% discount for first-time customers**. Please contact **+65 6294 8888** or **info@koloristsg.com** for consultations or bookings."
- Korean: "문의 주셔서 감사합니다. 저희 컬러링 서비스는 **짧은 머리 기준 150달러부터** 시작되며, 모발 길이, 상태, 시술 종류에 따라 가격이 달라질 수 있습니다. 현재 **첫 방문 고객님께 10% 할인 혜택**도 드리고 있습니다. 상담이나 예약은 **+65 6294 8888** 또는 **info@koloristsg.com**으로 문의해 주세요."

Promotion Details:
- English: "Thank you for your inquiry. We currently offer a **10% discount for first-time customers** on all coloring and treatment services. Contact **+65 6294 8888** or **info@koloristsg.com** to learn more or to make a booking."
- Korean: "문의 주셔서 감사합니다. 현재 모든 컬러링 및 트리트먼트 서비스에 대해 **첫 방문 고객님께 10% 할인 혜택**을 제공하고 있습니다. 자세한 문의나 예약은 **+65 6294 8888** 또는 **info@koloristsg.com**으로 연락해 주세요."

Booking/Reservation Process:
- English: "Thank you for your inquiry. You can book an appointment by calling **+65 6294 8888**, emailing **info@koloristsg.com**, or visiting us directly. We recommend booking at least **3 days in advance** for preferred time slots. Please let us know if you need assistance."
- Korean: "문의 주셔서 감사합니다. **+65 6294 8888**로 전화, **info@koloristsg.com** 이메일, 또는 직접 방문하여 예약이 가능합니다. 원하시는 시간대를 위해 **3일 전 예약**을 권장드립니다. 도움이 필요하시면 언제든지 알려주세요."

Cancellation Policy:
- English: "Thank you for your inquiry. Please inform us at least **24 hours in advance** if you wish to cancel to avoid charges. Contact **+65 6294 8888** or **info@koloristsg.com** for cancellations. Thank you for your understanding."
- Korean: "문의 주셔서 감사합니다. 예약 취소는 **시술 24시간 전까지** 알려주시면 수수료 없이 처리해 드립니다. **+65 6294 8888** 또는 **info@koloristsg.com**으로 연락해 주세요. 양해 부탁드립니다."

Hair Treatment Recommendation:
- English: "Thank you for your inquiry. We offer professional hair treatments such as **scalp detox, moisture repair, and keratin smoothing**. The ideal option depends on your hair condition and goals. We recommend a **complimentary consultation** for personalized advice. Contact **+65 6294 8888** or **info@koloristsg.com** to book."
- Korean: "문의 주셔서 감사합니다. 저희 살롱에서는 **두피 디톡스, 수분 케어, 케라틴 클리닉** 등의 트리트먼트를 제공합니다. 모발 상태와 스타일에 따라 가장 적합한 시술이 달라지므로, **무료 상담 예약**을 통해 전문 스타일리스트의 추천을 받으시기 바랍니다. 예약은 **+65 6294 8888** 또는 **info@koloristsg.com**으로 문의해 주세요."

Services Offered Inquiry:
- English: "Thank you for your inquiry. At Kolorist, we offer a full range of professional hair services, including: - **Hair Coloring** - **Haircuts & Styling** - **Scalp Treatments** - **Keratin Smoothing Treatments** - **Moisture & Repair Treatments** - **Hair Bleaching & Highlights** For detailed pricing and personalized recommendations, we recommend booking a **complimentary consultation** with our stylists. Feel free to contact us at **+65 6294 8888** or **info@koloristsg.com** for more information or reservations."
- Korean: "문의 주셔서 감사합니다. Kolorist에서는 다음과 같은 다양한 헤어 서비스를 제공하고 있습니다: - **헤어 컬러링** - **커트 및 스타일링** - **두피 케어** - **케라틴 클리닉** - **수분 & 손상 케어** - **탈색 및 하이라이트** 자세한 가격 안내와 고객님께 맞는 시술 추천을 위해 **무료 상담 예약**을 권장드립니다. **+65 6294 8888** 또는 **info@koloristsg.com**으로 문의 또는 예약해 주세요."

Important:
- Never default to Korean when the user's input is in English.
- Never default to English when the user's input is in Korean.
- Match the language of the user's input exactly unless explicitly instructed otherwise.

Annex D: 
Step 1 : Look for the knowledge under work space 
Step 2 : Under What are you trying to Achieve Paste below: 

Intent User Input Example Bot Response Source Page General Information What is Kolorist? Kolorist is a Korean beauty salon located at Orchard Gateway, Singapore, offering services like head spa, Korean makeup, personal color analysis, and more. https://kolorist.sg/ Service Information What services do you offer? We offer Head Spa & Facial, Korean Makeup, Personal Color Analysis, Damage Repair Treatment, and Head Spa Training. https://kolorist.sg/pages/services Booking Information How can I book an appointment? You can book online through our booking portal or contact us via WhatsApp. https://bookings.gettimely.com/koloristsg/book, https://api.whatsapp.com/send/?phone=6582184070 Contact Information How do I contact you? You can reach us via WhatsApp at +65 8218 4070. Our salon is located at Level 2, #02-01, Orchard Gateway, Singapore 238896. https://kolorist.sg/pages/contact-us-1 About Information What is Kolorist's mission? Our vision is to be a one-stop beauty haven, offering services like Korean makeup, self-photoshoots, and color analysis, making customers feel at home and confident. https://kolorist.sg/ Personal Color Analysis What is Personal Color Analysis? Personal Color Analysis identifies the best colors to enhance your natural features. Our certified Korean experts use patented tools and AI technology for precise results. https://kolorist.sg/pages/personal-colour-analysis Head Spa Services Tell me about your Head Spa services. Our Head Spa services include True Care Head Spa, Ayurveda Head Spa, and more, ranging from $120 to $260, providing deep cleansing and relaxation. https://kolorist.sg/pages/kolorist-head-spa Korean Makeup Services Do you offer Korean makeup services? Yes, our Korean makeup services are provided by professional Korean makeup experts, specializing in natural, glowing looks for events and weddings. https://kolorist.sg/pages/korean-make-up-services Damage Repair Treatment What is your Damage Repair Treatment? Our Damage Repair Treatment transforms damaged hair to silky smooth with effective solutions and rebonding treatments, priced at $188 for any hair length. https://kolorist.sg/pages/frizzy-lab Head Spa Training Do you offer Head Spa training? Yes, we offer Korean Head Spa training courses, including a 3-day course for $2,500 and a 5-day private lesson for $6,000, covering scalp massage and detoxification techniques. https://kolorist.sg/pages/korean-headspa-training Blog Information Do you have a blog? Yes, our blog covers topics like hair trends, gray root touch-ups, and achieving stunning hair color without damage. https://kolorist.sg/blogs/blog News Updates Any recent news? Our news section includes articles on anti-frizz solutions and other hair care tips to keep your hair healthy and stylish. https://kolorist.sg/blogs/news Product Information What products do you use? We use premium products like Milbon, Kerastase, and Olaplex for our treatments, ensuring quality and effective results. https://kolorist.sg/collections/all Pricing Information How much does a Head Spa cost? Our Head Spa services range from $120 to $260, depending on the type and duration. https://kolorist.sg/pages/services Operating Hours What are your operating hours? We are open Thursday to Tuesday from 10am to 8pm. We are closed on Wednesdays, except on public holidays. https://kolorist.sg/pages/contact-us-1 Location Information Where are you located? Our salon is located at Level 2, #02-01, Orchard Gateway, 227 Orchard Road, Singapore 238896. https://maps.app.goo.gl/SaiSjcHX3ZEnBKLHA Men's Services Do you offer services for men? Yes, we offer men's perm and hair services, including volume perm and down perm, tailored to different face shapes and preferences. https://kolorist.sg/pages/men-perm-bundle Hair Color Tips Any tips before coloring my hair? Before coloring your hair, consider factors like hair type and desired shade. Our blog provides essential advice to help you make informed decisions. https://kolorist.sg/blogs/blog/things-to-know-before-coloring-your-hair-for-the-first-time-a-beginners-guide Hair Extensions Do you offer hair extensions? While we don't offer hair extensions, our blog provides guidance on choosing the right color and texture for hair extensions. https://kolorist.sg/blogs/blog/how-to-choose-the-right-color-and-texture-of-hair-extensions Service Information What types of head spa treatments do you offer? We offer several head spa treatments including:\n- True Care Head Spa ($120, 60 mins)\n- Ayurveda Head Spa ($180, 90 mins)\n- Ayurveda Plus Head Spa ($220, 90 mins)\n- Head Spa + Scalp Care ($260, 120 mins) https://kolorist.sg/pages/kolorist-head-spa Service Information Can I get a facial treatment? Yes! We offer facials such as:\n- Relaxation Ritual Facial ($70)\n- Hydro Facial ($90)\n- Face Detox Facial ($130)\n- Crystal Cleanse Facial ($160)\n- Oxygen Infusion Facial ($190) https://kolorist.sg/pages/kolorist-head-spa Service Information Tell me more about your Korean makeup services. We offer:\n- Korean Natural Makeup: $200\n- Studio Style Makeup: $300\n- Event Makeup: $380\n- Korean Bridal Makeup: $480\nAdd-ons: Korean lashes ($40), eyebrow shaping ($30), styling options available. https://kolorist.sg/pages/korean-make-up-services Service Information Do you provide personal colour analysis? Yes! Sessions include a full draping test, makeup and styling guidance, and a take-home palette.\n- 1 Pax: $180 (60 mins)\n- 2 Pax: $320 (105 mins total) https://kolorist.sg/pages/personal-colour-analysis Blog Content What can I read on your blog? Our blog covers:\n- 2024 Hair Trends\n- Gray Root Maintenance\n- Hair Coloring Tips\n- Frizz Control Advice\n- Low-Maintenance Hair Color Ideas https://kolorist.sg/blogs/blog Social Media Where can I find you on social media? You can follow us on:\n- Instagram: https://www.instagram.com/kolorist.sg\n- TikTok: https://www.tiktok.com/@salon.kolorist.sg\n- Facebook: https://www.facebook.com/kolorist.sg https://www.instagram.com/kolorist.sg, https://www.tiktok.com/@salon.kolorist.sg, https://www.facebook.com/kolorist.sg FAQ How should I prepare for my personal colour analysis session? Come with a clean, makeup-free face if possible. Feel free to bring your makeup pouch or any specific items you'd like reviewed during the consultation. https://kolorist.sg/pages/personal-colour-analysis Training Do you offer training for head spa services? Yes, we provide professional training for Korean head spa treatments. The program includes hands-on sessions, certified instruction, and is suitable for salon professionals. https://kolorist.sg/pages/korean-headspa-training Service Information Can you explain the different head spa services? Kolorist offers a variety of head spa services:\n- True Care Head Spa (60 mins, $120): A rejuvenating treatment to relieve tension and promote scalp health.\n- Ayurveda Head Spa (90 mins, $180): Combines ancient Indian techniques for holistic relaxation.\n- Ayurveda Plus Head Spa (90 mins, $220): An enhanced version including facial care.\n- Head Spa + Scalp Care (120 mins, $260): A full experience with deep scalp detoxification and care. https://kolorist.sg/pages/kolorist-head-spa Service Information Tell me about your Korean makeup services. Kolorist provides various Korean makeup services:\n- Natural Make Up: $200\n- Studio Style Make Up: $300\n- ROM/Event/Gala Make Up: $380\n- Korean Bridal Make Up: $480\nAdd-ons include Korean eyelashes ($40), eyebrow shaping ($30), hairstyling (from $40), and morning surcharges. https://kolorist.sg/pages/korean-make-up-services Service Information What is the personal colour analysis? The Personal Colour Analysis identifies colours that complement your natural tone. Options:\n- Individual (60 mins): $180 (U.P. $250)\n- Duo (2 pax, 105 mins): $320 (U.P. $500) https://kolorist.sg/pages/personal-colour-analysis Blog & Content Do you have blog posts or hair care tips? Yes, Kolorist shares expert tips and trends on their blog. Topics include:\n- 2024 Hair Colour Trends\n- Haircare for Gray Roots\n- Root Retouch Importance\n- Colouring Advice by Hair Type\n- Low Maintenance Hair Ideas https://kolorist.sg/blogs/blog Social Media Where can I find you on social media? You can follow Kolorist on:\n- Instagram: @kolorist.sg\n- TikTok: @salon.kolorist.sg\n- Facebook: kolorist.sg https://www.instagram.com/kolorist.sg, https://www.facebook.com/kolorist.sg, https://www.tiktok.com/@salon.kolorist.sg Policy & Booking What's your cancellation policy or are walk-ins allowed? Appointments are preferred. Walk-ins are welcome based on availability. Please notify at least 24 hours in advance for cancellations or reschedules. https://kolorist.sg/ Head Spa Services What head spa treatments do you offer? We offer various Head Spa treatments including:\n- True Care Head Spa (60 mins) – $120\n- Ayurveda Head Spa (90 mins) – $180\n- Ayurveda Plus Head Spa (90 mins) – $220\n- Head Spa + Scalp Care (120 mins) – $260 https://kolorist.sg/pages/kolorist-head-spa Facial Services Tell me about your facial treatments. Our facial offerings include:\n- Relaxation Ritual Facial: $35 (add-on) / $70 (à la carte)\n- Hydro Facial: $45 (add-on) / $90 (à la carte)\n- Face Detox Facial: $65 (add-on) / $130 (à la carte)\n- Crystal Cleanse Facial: $80 (add-on) / $160 (à la carte)\n- Oxygen Infusion Facial: $95 (add-on) / $190 (à la carte) https://kolorist.sg/pages/kolorist-head-spa Korean Make Up Do you offer bridal or event makeup? Yes! Our Korean makeup services include:\n- Korean Natural Make Up: $200\n- Studio Style Make Up: $300\n- ROM/Gala/Event Make Up: $380\n- Korean Bridal Make Up: $480\nAdd-ons: Eyelashes ($40), Eyebrow Shaping ($30), Hairstyling ($40+) https://kolorist.sg/pages/korean-make-up-services Personal Colour Analysis What is personal colour analysis? We provide Personal Colour Analysis:\n- 1 pax: $180 (U.P. $250)\n- 2 pax: $320 (U.P. $500)\nIncludes a full Korean-style palette assessment. https://kolorist.sg/pages/personal-colour-analysis Blog and Hair Tips Do you have tips on hair colouring or trends? Yes! Visit our blog for hair tips and trends like:\n- 2024 Hair Colour Trends\n- How to maintain hair colour\n- Root touch-up timing and tips https://kolorist.sg/blogs/blog Social Media Where can I follow you on social media? Follow us for updates, promotions, and hair tips:\n- Instagram: @kolorist.sg\n- TikTok: @salon.kolorist.sg\n- Facebook: kolorist.sg https://www.instagram.com/kolorist.sg, https://www.tiktok.com/@salon.kolorist.sg, https://www.facebook.com/kolorist.sg

Step 3 : Save the above

Step 4 : Browse to knowledge once again and Tap on the Knowledge Created from above 

Step 5 : Under Search collection press the + button and upload all the relavant data (Excel sheets)

