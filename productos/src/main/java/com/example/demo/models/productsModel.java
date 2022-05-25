package com.example.demo.models;

import javax.persistence.*;
import java.io.Serializable;
import java.sql.Blob;

@Entity
@Table(name="productos")
public class productsModel implements Serializable{

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "id_pro")
    private int id_pro;
    @Column(name = "nom_pro")
    private String nom_pro;
    @Column(name = "des_pro")
    private String des_pro;
    @Column(name = "pric_pro")
    private String pric_pro;
    @Column(name = "stock_pro")
    private int stock_pro;
    @Column(name = "desc_pro")
    private int desc_pro;
    @Lob
    @Column(name = "img_pro")
    private byte[] img_pro;
    @ManyToOne
    @JoinColumn(name = "tipo.id_tipo")
    private tipoModel tipo;

    public productsModel() {
    }

    public productsModel(int id_pro, String nom_pro, String des_pro, String pric_pro, int stock_pro, int desc_pro, byte[] img_pro, tipoModel tipo) {
        this.id_pro = id_pro;
        this.nom_pro = nom_pro;
        this.des_pro = des_pro;
        this.pric_pro = pric_pro;
        this.stock_pro = stock_pro;
        this.desc_pro = desc_pro;
        this.img_pro = img_pro;
        this.tipo = tipo;
    }

    public int getId_pro() {
        return id_pro;
    }

    public void setId_pro(int id_pro) {
        this.id_pro = id_pro;
    }

    public String getNom_pro() {
        return nom_pro;
    }

    public void setNom_pro(String nom_pro) {
        this.nom_pro = nom_pro;
    }

    public String getDes_pro() {
        return des_pro;
    }

    public void setDes_pro(String des_pro) {
        this.des_pro = des_pro;
    }

    public String getPric_pro() {
        return pric_pro;
    }

    public void setPric_pro(String pric_pro) {
        this.pric_pro = pric_pro;
    }

    public int getStock_pro() {
        return stock_pro;
    }

    public void setStock_pro(int stock_pro) {
        this.stock_pro = stock_pro;
    }

    public int getDesc_pro() {
        return desc_pro;
    }

    public void setDesc_pro(int desc_pro) {
        this.desc_pro = desc_pro;
    }

    public byte[] getImg_pro() {
        return img_pro;
    }

    public void setImg_pro(byte[] img_pro) {
        this.img_pro = img_pro;
    }

    public tipoModel getTipo() {
        return tipo;
    }

    public void setTipo(tipoModel tipo) {
        this.tipo = tipo;
    }
}
