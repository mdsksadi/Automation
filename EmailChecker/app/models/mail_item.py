"""
/**
 * @file mail_item.py
 * @author Shekh Sadi
 * @date 2025-10-31
 * @brief Data model for a single email item.
 */
"""

from dataclasses import dataclass

@dataclass
class MailItem:
    uid: str
    from_: str
    subject: str
    date: str