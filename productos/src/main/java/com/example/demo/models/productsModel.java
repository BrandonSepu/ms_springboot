package com.example.demo.models;

import javax.persistence.*;
import java.io.Serializable;

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
    @Column(name = "tipo_id_tipo")
    private String tipo_id_tipo;

    public productsModel() {
    }

    public productsModel(String nom_pro, String des_pro, String pric_pro, String tipo_id_tipo) {
        this.nom_pro = nom_pro;
        this.des_pro = des_pro;
        this.pric_pro = pric_pro;
        this.tipo_id_tipo = tipo_id_tipo;
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

    public String getTipo_id_tipo() {
        return tipo_id_tipo;
    }

    public void setTipo_id_tipo(String tipo_id_tipo) {
        this.tipo_id_tipo = tipo_id_tipo;
    }
}
