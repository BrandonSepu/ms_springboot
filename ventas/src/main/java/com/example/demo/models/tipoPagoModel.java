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
    @Column(name = "pago_tpag")
    private String pago_tpag;

    public tipoPagoModel() {
    }

    public tipoPagoModel(String pago_tpag) {
        this.pago_tpag = pago_tpag;
    }

    public int getId_tpag() {
        return id_tpag;
    }

    public void setId_tpag(int id_tpag) {
        this.id_tpag = id_tpag;
    }

    public String getPago_tpag() {
        return pago_tpag;
    }

    public void setPago_tpag(String pago_tpag) {
        this.pago_tpag = pago_tpag;
    }
}
