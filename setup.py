#!/usr/bin/env python3
"""
اسکریپت راه‌اندازی اولیه ربات مانیتور تلگرام
این اسکریپت اطلاعات لازم را از کاربر دریافت می‌کند و فایل user_config.json را ایجاد می‌کند
"""

import asyncio
import json
from telethon import TelegramClient
from telethon.sessions import StringSession

CONFIG_FILE = 'user_config.json'

def get_user_input():
    """دریافت اطلاعات از کاربر با اعتبارسنجی"""
    print("\n" + "="*60)
    print("🤖 راه‌اندازی اولیه ربات مانیتور تلگرام")
    print("="*60 + "\n")
    
    print("📝 لطفاً اطلاعات خود را وارد کنید:\n")
    
    # دریافت و اعتبارسنجی API ID
    while True:
        api_id = input("🔑 API ID خود را وارد کنید (از my.telegram.org): ").strip()
        if api_id.isdigit() and len(api_id) > 0:
            api_id = int(api_id)
            break
        else:
            print("❌ API ID باید یک عدد باشد. دوباره تلاش کنید.\n")
    
    # دریافت و اعتبارسنجی API HASH
    while True:
        api_hash = input("🔐 API HASH خود را وارد کنید (از my.telegram.org): ").strip()
        if len(api_hash) > 0:
            break
        else:
            print("❌ API HASH نمی‌تواند خالی باشد. دوباره تلاش کنید.\n")
    
    # دریافت و اعتبارسنجی شماره تلفن
    while True:
        phone = input("📱 شماره همراه خود را با +98 وارد کنید (مثال: +989123456789): ").strip()
        if len(phone) > 0:
            if not phone.startswith('+'):
                if phone.startswith('98'):
                    phone = '+' + phone
                elif phone.startswith('0'):
                    phone = '+98' + phone[1:]
                else:
                    phone = '+98' + phone
            break
        else:
            print("❌ شماره تلفن نمی‌تواند خالی باشد. دوباره تلاش کنید.\n")
    
    # دریافت و اعتبارسنجی توکن ربات
    while True:
        bot_token = input("🤖 توکن ربات تلگرام خود را وارد کنید (از @BotFather): ").strip()
        if len(bot_token) > 0:
            break
        else:
            print("❌ توکن ربات نمی‌تواند خالی باشد. دوباره تلاش کنید.\n")
    
    return {
        'api_id': api_id,
        'api_hash': api_hash,
        'phone': phone,
        'bot_token': bot_token,
        'session': ''
    }

async def setup():
    """راه‌اندازی اولیه و ایجاد session"""
    config = get_user_input()
    
    print("\n" + "="*60)
    print("🔐 در حال اتصال به تلگرام برای ایجاد session...")
    print("="*60 + "\n")
    
    # ایجاد کلاینت موقت برای احراز هویت
    client = TelegramClient(
        StringSession(),
        config['api_id'],
        config['api_hash']
    )
    
    try:
        await client.start(phone=config['phone'])
        
        # دریافت session string
        session_string = client.session.save()
        config['session'] = session_string
        
        print("\n✅ احراز هویت موفقیت‌آمیز بود!")
        
        # ذخیره تنظیمات
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        
        print(f"💾 فایل تنظیمات در {CONFIG_FILE} ذخیره شد")
        
        print("\n" + "="*60)
        print("✅ راه‌اندازی با موفقیت انجام شد!")
        print("="*60 + "\n")
        
        print("📋 مراحل بعدی:")
        print("1. ربات را با دستور 'python main.py' اجرا کنید")
        print("2. به ربات خود در تلگرام پیام دهید و /start را بزنید")
        print("3. از /help برای مشاهده راهنما استفاده کنید")
        
        print("\n⚠️  نکات امنیتی:")
        print(f"- فایل {CONFIG_FILE} حاوی اطلاعات حساس شماست")
        print("- هرگز این فایل را با دیگران به اشتراک نگذارید")
        print("- از این فایل نسخه پشتیبان تهیه کنید")
        
        await client.disconnect()
        
    except Exception as e:
        print(f"\n❌ خطا رخ داد: {e}")
        print("\n💡 لطفاً اطلاعات وارد شده را بررسی کنید و دوباره تلاش کنید.")

if __name__ == '__main__':
    try:
        asyncio.run(setup())
    except KeyboardInterrupt:
        print("\n\n👋 راه‌اندازی لغو شد.")
    except Exception as e:
        print(f"\n❌ خطا رخ داد: {e}")
