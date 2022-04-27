package com.example.demo.models;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name="bodega")
public class bodegaModel implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "id_bod")
    private int id_bod;
    @Column(name = "stock_bod")
    private String stock_bod;
    @Column(name = "producto_id")
    private String producto_id;

    public bodegaModel() {
    }

    public bodegaModel(String stock_bod, String producto_id) {
        this.stock_bod = stock_bod;
        this.producto_id = producto_id;
    }

    public int getId_bod() {
        return id_bod;
    }

    public void setId_bod(int id_bod) {
        this.id_bod = id_bod;
    }

    public String getStock_bod() {
        return stock_bod;
    }

    public void setStock_bod(String stock_bod) {
        this.stock_bod = stock_bod;
    }

    public String getProducto_id() {
        return producto_id;
    }

    public void setProducto_id(String producto_id) {
        this.producto_id = producto_id;
    }
}
