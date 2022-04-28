package com.example.demo.models;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name="ventas")
public class ventasModel implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "id_ventas")
    private int id_ventas;
    @Column(name = "product_id")
    private String product_id;
    @Column(name = "user_id")
    private String user_id;
    @Column(name = "detalle_ven_id_detven")
    private String detalle_ven_id_detven;

    public ventasModel() {
    }

    public ventasModel(String product_id, String user_id, String detalle_ven_id_detven) {
        this.product_id = product_id;
        this.user_id = user_id;
        this.detalle_ven_id_detven = detalle_ven_id_detven;
    }

    public int getId_ventas() {
        return id_ventas;
    }

    public void setId_ventas(int id_ventas) {
        this.id_ventas = id_ventas;
    }

    public String getProduct_id() {
        return product_id;
    }

    public void setProduct_id(String product_id) {
        this.product_id = product_id;
    }

    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }

    public String getDetalle_ven_id_detven() {
        return detalle_ven_id_detven;
    }

    public void setDetalle_ven_id_detven(String detalle_ven_id_detven) {
        this.detalle_ven_id_detven = detalle_ven_id_detven;
    }
}
