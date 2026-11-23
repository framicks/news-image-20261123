#!/usr/bin/env python3
"""Menyalin gambar sampul berita ke direktori keluaran make.fun.

Skrip ini mencari ``front-page.png`` di direktori yang sama dengan
skrip, memeriksa delapan byte pertamanya terhadap tanda tangan PNG,
kemudian menyalin berkas itu menjadi ``entry.png`` di dalam direktori
keluaran.

Direktori keluaran dibaca dari variabel lingkungan
``MAKEFUN_OUTPUT_DIR``; kalau variabel itu kosong atau tidak ada,
dipakai ``/output``. Skrip hanya memakai pustaka standar Python dan
tidak pernah mengakses jaringan.
"""

import os
import shutil
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
SOURCE_NAME = "front-page.png"
TARGET_NAME = "entry.png"
DEFAULT_OUTPUT = "/output"


def find_source():
    """Kembalikan path absolut gambar yang duduk di samping skrip."""
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, SOURCE_NAME)


def pick_output_dir():
    """Pilih direktori keluaran dari environment, atau pakai default."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return value or DEFAULT_OUTPUT


def has_png_signature(path):
    """Baca delapan byte pertama dan bandingkan dengan tanda PNG."""
    with open(path, "rb") as stream:
        prefix = stream.read(len(PNG_SIGNATURE))
    return prefix == PNG_SIGNATURE


def duplicate_file(source, target):
    """Salin berkas sumber ke tujuan, kembalikan ukuran byte hasil."""
    shutil.copyfile(source, target)
    return os.path.getsize(target)


def run():
    """Lakukan penyalinan; 0 bila berhasil, 1 bila ada masalah."""
    source = find_source()
    if not os.path.isfile(source):
        print(f"error: berkas sumber tidak ada: {source}", file=sys.stderr)
        return 1
    if not has_png_signature(source):
        print(f"error: {source} bukan berkas PNG", file=sys.stderr)
        return 1
    out_dir = pick_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, TARGET_NAME)
    size = duplicate_file(source, target)
    print(f"ok: {size} byte disalin ke {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
