package com.example.demo.models;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name="tipopago")
public class tipoPagoModel implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "id_tpag")
    private int id_tpag;
    @Column(name = "pago")
    private String nom_tipo;

    public tipoPagoModel() {
    }

    public tipoPagoModel(String nom_tipo) {
        this.nom_tipo = nom_tipo;
    }

    public int getId_tipo() {
        return id_tipo;
    }

    public void setId_tipo(int id_tipo) {
        this.id_tipo = id_tipo;
    }

    public String getNom_tipo() {
        return nom_tipo;
    }

    public void setNom_tipo(String nom_tipo) {
        this.nom_tipo = nom_tipo;
    }
}
