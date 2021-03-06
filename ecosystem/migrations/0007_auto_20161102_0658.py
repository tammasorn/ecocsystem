# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecosystem', '0006_auto_20161102_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('robot_model', models.CharField(choices=[('Mini-White', 'Mini-White')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='province',
            field=models.CharField(choices=[('กรุงเทพมหานคร', 'กรุงเทพมหานคร'), ('กระบี่', 'กระบี่'), ('กาญจนบุรี', 'กาญจนบุรี'), ('กาฬสินธุ์', 'กาฬสินธุ์'), ('กำแพงเพชร', 'กำแพงเพชร'), ('ขอนแก่น', 'ขอนแก่น'), ('จันทบุรี', 'จันทบุรี'), ('ฉะเชิงเทรา', 'ฉะเชิงเทรา'), ('ชัยนาท', 'ชัยนาท'), ('ชัยภูมิ', 'ชัยภูมิ'), ('ชุมพร', 'ชุมพร'), ('ชลบุรี', 'ชลบุรี'), ('เชียงใหม่', 'เชียงใหม่'), ('เชียงราย', 'เชียงราย'), ('ตรัง', 'ตรัง'), ('ตราด', 'ตราด'), ('ตาก', 'ตาก'), ('นครนายก', 'นครนายก'), ('นครปฐม', 'นครปฐม'), ('นครพนม', 'นครพนม'), ('นครราชสีมา', 'นครราชสีมา'), ('นครศรีธรรมราช', 'นครศรีธรรมราช'), ('นครสวรรค์', 'นครสวรรค์'), ('นราธิวาส', 'นราธิวาส'), ('น่าน', 'น่าน'), ('นนทบุรี', 'นนทบุรี'), ('บึงกาฬ', 'บึงกาฬ'), ('บุรีรัมย์', 'บุรีรัมย์'), ('ประจวบคีรีขันธ์', 'ประจวบคีรีขันธ์'), ('ปทุมธานี', 'ปทุมธานี'), ('ปราจีนบุรี', 'ปราจีนบุรี'), ('ปัตตานี', 'ปัตตานี'), ('พะเยา', 'พะเยา'), ('พระนครศรีอยุธยา', 'พระนครศรีอยุธยา'), ('พังงา', 'พังงา'), ('พิจิตร', 'พิจิตร'), ('พิษณุโลก', 'พิษณุโลก'), ('เพชรบุรี', 'เพชรบุรี'), ('เพชรบูรณ์', 'เพชรบูรณ์'), ('แพร่', 'แพร่'), ('พัทลุง', 'พัทลุง'), ('ภูเก็ต', 'ภูเก็ต'), ('มหาสารคาม', 'มหาสารคาม'), ('มุกดาหาร', 'มุกดาหาร'), ('แม่ฮ่องสอน', 'แม่ฮ่องสอน'), ('ยโสธร', 'ยโสธร'), ('ยะลา', 'ยะลา'), ('ร้อยเอ็ด', 'ร้อยเอ็ด'), ('ระนอง', 'ระนอง'), ('ระยอง', 'ระยอง'), ('ราชบุรี', 'ราชบุรี'), ('ลพบุรี', 'ลพบุรี'), ('ลำปาง', 'ลำปาง'), ('ลำพูน', 'ลำพูน'), ('เลย', 'เลย'), ('ศรีสะเกษ', 'ศรีสะเกษ'), ('สกลนคร', 'สกลนคร'), ('สงขลา', 'สงขลา'), ('สมุทรสาคร', 'สมุทรสาคร'), ('สมุทรปราการ', 'สมุทรปราการ'), ('สมุทรสงคราม', 'สมุทรสงคราม'), ('สระแก้ว', 'สระแก้ว'), ('สระบุรี', 'สระบุรี'), ('สิงห์บุรี', 'สิงห์บุรี'), ('สุโขทัย', 'สุโขทัย'), ('สุพรรณบุรี', 'สุพรรณบุรี'), ('สุราษฎร์ธานี', 'สุราษฎร์ธานี'), ('สุรินทร์', 'สุรินทร์'), ('สตูล', 'สตูล'), ('หนองคาย', 'หนองคาย'), ('หนองบัวลำภู', 'หนองบัวลำภู'), ('อำนาจเจริญ', 'อำนาจเจริญ'), ('อุดรธานี', 'อุดรธานี'), ('อุตรดิตถ์', 'อุตรดิตถ์'), ('อุทัยธานี', 'อุทัยธานี'), ('อุบลราชธานี', 'อุบลราชธานี'), ('อ่างทอง', 'อ่างทอง')], max_length=100),
        ),
        migrations.AddField(
            model_name='modelregister',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecosystem.Register'),
        ),
    ]
