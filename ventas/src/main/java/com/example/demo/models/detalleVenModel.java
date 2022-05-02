package com.example.demo.models;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name="detalle_ven")
public class detalleVenModel implements Serializable{

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "id_detven")
    private int id_detven;
    @Column(name = "producto_det")
    private String producto_det;
    @Column(name = "user_det")
    private String user_det;
    @Column(name = "hora_det")
    private String hora_det;
    @Column(name = "fecha_det")
    private String fecha_det;
    @Column(name = "tipopago_id_tpag")
    private String tipopago_id_tpag;

    public detalleVenModel() {
    }

    public detalleVenModel(String producto_det, String user_det, String hora_det, String fecha_det, String tipopago_id_tpag) {
        this.producto_det = producto_det;
        this.user_det = user_det;
        this.hora_det = hora_det;
        this.fecha_det = fecha_det;
        this.tipopago_id_tpag = tipopago_id_tpag;
    }

    public int getId_ven() {
        return id_detven;
    }

    public void setId_ven(int id_detven) {
        this.id_detven = id_detven;
    }

    public String getProducto_det() {
        return producto_det;
    }

    public void setProducto_det(String producto_det) {
        this.producto_det = producto_det;
    }

    public String getUser_det() {
        return user_det;
    }

    public void setUser_det(String user_det) {
        this.user_det = user_det;
    }

    public String getHora_det() {
        return hora_det;
    }

    public void setHora_det(String hora_det) {
        this.hora_det = hora_det;
    }

    public String getFecha_det() {
        return fecha_det;
    }

    public void setFecha_det(String fecha_det) {
        this.fecha_det = fecha_det;
    }

    public String getTipopago_id_tpag() {
        return tipopago_id_tpag;
    }

    public void setTipopago_id_tpag(String tipopago_id_tpag) {
        this.tipopago_id_tpag = tipopago_id_tpag;
    }
}
