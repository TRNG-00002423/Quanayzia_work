package org.garden.dao;

import org.garden.domain.Product;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public final class JdbcProductDao implements ProductDao {
    private final Connection connection;

    public JdbcProductDao(Connection connection) {
        this.connection = connection;
    }

    @Override
    public long insert(Product product) throws Exception {
        // Insert statement
        String INSERT_PRODUCT_SQL= "INSERT INTO product(sku, name, price,stock_qty) " +
                "values(?,?,?,?)";

        try(PreparedStatement ps=connection.prepareStatement(INSERT_PRODUCT_SQL,
                    Statement.RETURN_GENERATED_KEYS)) {

                ps.setString(1, product.sku());
                ps.setString(2, product.name());
                ps.setDouble(3, product.price());
                ps.setInt(4, product.stockQty());
                ps.executeUpdate();

                try(ResultSet rs=ps.getGeneratedKeys()){
                    if(rs.next()){
                        return  rs.getLong(1);
                    }
                }
            throw new SQLException("Failed to insert product");

            }


    }

    @Override
    public Optional<Product> findBySku(String sku) throws Exception {
        String sql = "SELECT id, sku, name, price, stock_qty FROM product WHERE sku = ?";
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setString(1, sku);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(mapRow(rs));
                }
            }
        }
        return Optional.empty();
    }

    @Override
    public List<Product> findAll() throws Exception {
        List<Product> out = new ArrayList<>();
        String sql = "SELECT id, sku, name, price, stock_qty FROM product ORDER BY id";
        try (PreparedStatement ps = connection.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                out.add(mapRow(rs));
            }
        }
        return out;
    }

    @Override
    public void updateStock(String sku, int newQty) throws Exception {
        String PRODOCT_UPDATE= "UPDATE product SET stock_qty=? WHERE sku=?";

        try(PreparedStatement ps=connection.prepareStatement(PRODOCT_UPDATE)){

            ps.setInt(1, newQty);
            ps.setString(2, sku);

            int rowsUpdated = ps.executeUpdate();

            if(rowsUpdated==0){
                throw new SQLException("No product found with this sku: "+ sku);
            }
        }
    }

    @Override
    public void deleteBySku(String sku) throws Exception {
        String DELETE_BY_SKU = "DELETE FROM product WHERE sku = ?";

        try(PreparedStatement ps= connection.prepareStatement(DELETE_BY_SKU)){

            ps.setString(1,sku);

            int rowsDeleted=ps.executeUpdate(); // it returns a count
            //0 nothing matched or missu=ing record
            // 1 is success
            // >1 data integrity issue

            if(rowsDeleted==0){
                throw new SQLException("No Product fround with SKU "+sku);
            }
        }
    }

    private static Product mapRow(ResultSet rs) throws Exception {
        return new Product(
                rs.getLong("id"),
                rs.getString("sku"),
                rs.getString("name"),
                rs.getDouble("price"),
                rs.getInt("stock_qty"));
    }
}

