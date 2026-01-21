import random
from flask import Flask, render_template, request, url_for, redirect , jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from datetime import  date

app = Flask(__name__)


class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class StudentPost(db.Model):
    __tablename__ = "mahasiswa"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("list_dosen.id"))
    author = relationship("List_Dosen", back_populates="list_dos")
    NPM: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    Nama_Lengkap: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    mata_kuliah_mahasiswa: Mapped[str] = mapped_column(String(250), nullable=False)

class List_Dosen(db.Model):
    __tablename__ = "list_dosen"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    list_dos = relationship("StudentPost", back_populates="author")
    NIP_NIDN: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    Nama_Dosen: Mapped[str] = mapped_column(String(250), nullable=False)
    mata_kuliah_dosen: Mapped[str] = mapped_column(String(250), nullable=False)

class Dosen(db.Model):
    __tablename__ = "dosen"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    NIP_NIDN: Mapped[str] = mapped_column(String(100), unique=True)
    Nama_Dosen: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    mata_kuliah_dosen: Mapped[str] = mapped_column(String(250), nullable=False)
    dosen_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("matkul.id"))
    maha_dos = relationship("Mata_Kuliah", back_populates="dos_matkul")

class Mata_Kuliah(db.Model):
    __tablename__ = "matkul"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Matkul: Mapped[str] = mapped_column(String(100), unique=True)
    dos_matkul = relationship("Dosen", back_populates="maha_dos")


with app.app_context():
    db.create_all()
@app.route('/')
def main():
    return render_template("absensi.html",mahas=db.session.execute(db.select(List_Dosen)).scalars().all(),dos=db.session.execute(db.select(Mata_Kuliah)).scalars().all(),len=len,all_data=db.session.execute(db.select(StudentPost)).scalars().all())

@app.route("/input_mahasiswa",methods=["POST"])
def mahas_input():
    if request.method == "POST":
        new_post = StudentPost(
            author=db.session.query(List_Dosen).get(db.session.execute(db.select(List_Dosen).where(List_Dosen.Nama_Dosen == request.form.get("2T"))).scalar().id),
            NPM=request.form["Nomor_Pokok"],
            Nama_Lengkap=request.form["Nama_Lengkap"],
            date=date.today().strftime("%B %d, %Y"),
            mata_kuliah_mahasiswa=request.form.get("1T"),
        )
        db.session.add(new_post)
        db.session.commit()
    return redirect(url_for("main"))

@app.route("/input_dosen",methods=["POST"])
def dosen_input():
    if request.method == "POST":
        new_post = Dosen(
            NIP_NIDN=request.form.get("T2"),
            Nama_Dosen=request.form.get("T1"),
            date=date.today().strftime("%B %d, %Y"),
            mata_kuliah_dosen=request.form.get("T3"),
            maha_dos=db.session.query(Mata_Kuliah).get(db.session.execute(db.select(Mata_Kuliah).where(Mata_Kuliah.Matkul == request.form.get("T3"))).scalar().id),
        )
        db.session.add(new_post)
        db.session.commit()
    return  redirect(url_for("main"))

@app.route("/random")
def database():
    num = random.randint(1,max(db.session.query(StudentPost.id).all())[0])
    return jsonify(mahasiswa={
        "NPM":db.get_or_404(StudentPost,num).NPM,
        "Nama Lengkap":db.get_or_404(StudentPost,num).Nama_Lengkap,
        "date":db.get_or_404(StudentPost,num).date,
        "mata_kuliah_mahasiswa":db.get_or_404(StudentPost,num).mata_kuliah_mahasiswa,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)