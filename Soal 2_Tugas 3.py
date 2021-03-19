Biodata = {"nama" : "Alya Ramadhani",
           "hobi1" : "mendengarkan musik",
           "hobi2" : "nonton film",
           "hobi3" : "jalan-jalan",
           "sosmed1" : "alyaaaaaaakk",
           "sosmed2" : "aalyar",
           "sosmed3" : "i_m_alyak",
           "lagu_favorit1" : "dark_clouds",
           "lagu_favorit2" : "orange",
           "lagu_favorit3" : "don't_run_away",
           "makanan_favorit1" : "coklat",
           "makanan_favorit2" : "nasi goreng",
           "makanan_favorit3" : "dimsum",
           }

print(Biodata)
print("Nama saya adalah %s" % Biodata["nama"])
print("Saya memiliki hobi %s" % Biodata["hobi1"], ", %s" % Biodata["hobi2"], ", dan %s" % Biodata["hobi3"])
print("Main account instagram saya : %s" % Biodata["sosmed1"])
print("2nd account instagram saya : %s" % Biodata["sosmed2"])
print("3rd account insatgram saya : %s" % Biodata["sosmed3"])
print("Saya suka mendengarkan lagu yang berjudul %s" % Biodata["lagu_favorit1"], ", %s" % Biodata["lagu_favorit2"], ", dan %s" % Biodata["lagu_favorit3"])
print("Makanan favorit saya adalah %s" % Biodata["makanan_favorit1"], ", %s" % Biodata["makanan_favorit2"], ", dan %s" % Biodata["makanan_favorit3"])

Biodata["hobi1"] = "makan"
print(Biodata)

Biodata["sosmed2"] = "7xkxkkck"
print(Biodata)

Biodata.pop("makanan_favorit1")
print(Biodata)

Biodata.pop("makanan_favorit2")
print(Biodata)

Biodata["hobi_lain"] = "decor"
print(Biodata)
