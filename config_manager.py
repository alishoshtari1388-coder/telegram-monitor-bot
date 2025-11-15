import json
import os
from datetime import datetime

class ConfigManager:
    def __init__(self):
        self.config_file = 'user_config.json'
        self.targets_file = 'targets_config.json'

    def load_config(self):
        """بارگذاری تنظیمات از فایل"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None

    def save_config(self, config):
        """ذخیره تنظیمات در فایل"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

    def load_targets(self):
        """بارگذاری هدف‌ها و مقصدها"""
        try:
            with open(self.targets_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'targets': [], 'forward_to': None}

    def save_targets(self, targets_config):
        """ذخیره هدف‌ها و مقصدها"""
        with open(self.targets_file, 'w', encoding='utf-8') as f:
            json.dump(targets_config, f, ensure_ascii=False, indent=2)

    def add_target(self, user_id, username=""):
        """اضافه کردن کاربر هدف"""
        config = self.load_targets()
        targets = config.get('targets', [])

        # چک کردن تکراری نبودن
        for target in targets:
            if target['user_id'] == user_id:
                return False

        targets.append({
            'user_id': user_id,
            'username': username,
            'added_at': datetime.now().isoformat()
        })

        config['targets'] = targets
        self.save_targets(config)
        return True

    def remove_target(self, user_id):
        """حذف کاربر هدف"""
        config = self.load_targets()
        targets = config.get('targets', [])

        new_targets = [t for t in targets if t['user_id'] != user_id]

        if len(new_targets) == len(targets):
            return False  # کاربر پیدا نشد

        config['targets'] = new_targets
        self.save_targets(config)
        return True

    def set_forward(self, chat_id):
        """تنظیم مقصد فوروارد"""
        config = self.load_targets()
        config['forward_to'] = chat_id
        self.save_targets(config)
        return True

    def get_targets_list(self):
        """دریافت لیست کاربران هدف"""
        config = self.load_targets()
        return config.get('targets', [])

    def get_forward_chat(self):
        """دریافت مقصد فوروارد"""
        config = self.load_targets()
        return config.get('forward_to')
