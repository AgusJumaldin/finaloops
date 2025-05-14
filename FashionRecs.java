import java.awt.*;
import java.io.IOException;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;

public class FashionRecs extends JFrame {

    public FashionRecs() {
        setTitle("Skin Tone Analysis");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        Font titleFont = new Font("SansSerif", Font.BOLD, 32);
        Font bodyFont = new Font("Serif", Font.BOLD, 22);

        // ===== TOP BAR =====
        JPanel topBar = new JPanel();
        topBar.setBackground(new Color(255, 240, 245));
        topBar.setLayout(new BorderLayout());
        topBar.setPreferredSize(new Dimension(getWidth(), 60));

        // Title
        JLabel titleLabel = new JLabel("Skin Tone App");
        titleLabel.setForeground(Color.BLACK);
        titleLabel.setFont(titleFont);
        titleLabel.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 10));
        topBar.add(titleLabel, BorderLayout.WEST);

        // Right Panel for Buttons
        JPanel rightPanel = new JPanel();
        rightPanel.setOpaque(false);
        rightPanel.setLayout(new FlowLayout(FlowLayout.RIGHT, 20, 10));
        String[] buttons = {"Camera", "Fashion"};
        for (String name : buttons) {
            JButton button = new JButton(name);
            button.setFocusPainted(false);
            button.setFont(new Font("Monospaced", Font.BOLD, 17));
            button.setBackground(new Color(200, 200, 200));
            button.setForeground(Color.BLACK);
            button.setPreferredSize(new Dimension(120, 40));

            if (name.equals("Camera")) {
                button.addActionListener(e -> { 
                   try {
                        ProcessBuilder pb = new ProcessBuilder("python", "D:\\Code\\finalges-main\\src\\atas.py");
                        pb.redirectErrorStream(true);
                        Process process = pb.start();
                        
                        int exitCode = process.waitFor();
                        System.out.println("Python script exited with code: " + exitCode);
                        
                    } catch (IOException | InterruptedException ex) {
                        ex.printStackTrace();
                        JOptionPane.showMessageDialog(this, 
                            "Error running Python script: " + ex.getMessage(),
                            "Error", 
                            JOptionPane.ERROR_MESSAGE);
                    }
                });
            }           

            rightPanel.add(button);
        }
        topBar.add(rightPanel, BorderLayout.EAST);
        add(topBar, BorderLayout.NORTH);

        // ===== CENTER PANEL =====
        JPanel centerPanel = new JPanel();
        centerPanel.setLayout(new BoxLayout(centerPanel, BoxLayout.Y_AXIS));
        centerPanel.setBorder(new EmptyBorder(20, 20, 20, 20));
        centerPanel.setBackground(new Color(255, 210, 220));

        // Banner
        String bannerPath = "C:/Users/student/Documents/campus/4thSemester/OOP/images/banner.jpg";
        ImageIcon bannerIcon = new ImageIcon(bannerPath);
        if (bannerIcon.getIconWidth() > 0) {
            Image scaled = bannerIcon.getImage().getScaledInstance(1000, 400, Image.SCALE_SMOOTH);
            JLabel banner = new JLabel(new ImageIcon(scaled));
            banner.setAlignmentX(Component.LEFT_ALIGNMENT);
            banner.setBorder(new EmptyBorder(0, 0, 20, 0));
            centerPanel.add(banner);
        }

        String[] descriptions = {
                "Tone 2: FAIR COOL UNDERTONE\n"
                + "Powerstay 24H Weightless Liquid Foundation N10 MARBLE\n\n"
                + "Make Over Powerstay Total Cover Matte Cream Foundation 12G N10 MARBLE\n\n"
                + "Make Over Powerstay Demi-Matte Cover Cushion N10 MARBLE\n\n"
                + "Make Over Powerstay Total Cover Liquid Concealer 6.5 Ml 02 LIGHT TO MEDIUM\n\n"
                + "Make Over Powerstay 24H Matte Powder Foundation W41 CORAL SAND\n\n"
                + "Make Over Perfect Cover Two Way Cake 01 LACE",
            
                "Tone 3: FAIR TO LIGHT NEUTRAL UNDERTONE\n"
                + "Powerstay 24H Weightless Liquid Foundation W12 WARM MARBLE\n\n"
                + "Make Over Powerstay Total Cover Matte Cream Foundation 12G W12 WARM MARBLE\n\n"
                + "Make Over Powerstay Demi-Matte Cover Cushion W12 WARM MARBLE\n\n"
                + "Make Over Powerstay Total Cover Liquid Concealer 6.5 Ml 01 LIGHT\n\n"
                + "Make Over Powerstay 24H Matte Powder Foundation W12 WARM MARBLE\n\n"
                + "Make Over Perfect Cover Two Way Cake 08 HONEY",
            
                "Tone 4: LIGHT TO MEDIUM NEUTRAL UNDERTONE\n"
                + "Powerstay 24H Weightless Liquid Foundation N30 NATURAL BEIGE\n\n"
                + "Make Over Powerstay Total Cover Matte Cream Foundation 12G N30 NATURAL BEIGE\n\n"
                + "Make Over Powerstay Demi-Matte Cover Cushion N30 NATURAL BEIGE\n\n"
                + "Make Over Powerstay Total Cover Liquid Concealer 6.5 Ml LIGHT TO MEDIUM\n\n"
                + "Make Over Powerstay 24H Matte Powder Foundation N30 NATURAL BEIGE\n\n"
                + "Make Over Perfect Cover Two Way Cake 03 MAPLE",
            
                "Tone 5: LIGHT MEDIUM TO WARM PEACHY\n"
                + "Powerstay 24H Weightless Liquid Foundation W42 WARM SAND\n\n"
                + "Make Over Powerstay Total Cover Matte Cream Foundation 12G W42 WARM SAND\n\n"
                + "Make Over Powerstay Demi-Matte Cover Cushion W33 HONEY BEIGE\n\n"
                + "Make Over Powerstay Total Cover Liquid Concealer 6.5 Ml LIGHT TO MEDIUM\n\n"
                + "Make Over Powerstay 24H Matte Powder Foundation W42 WARM SAND\n\n"
                + "Make Over Perfect Cover Two Way Cake 04 DESERT",
            
                "Tone 6: MEDIUM WITH WARM GOLDEN UNDERTONE\n"
                + "Powerstay 24H Weightless Liquid Foundation W52 WARM TAN\n\n"
                + "Make Over Powerstay Total Cover Matte Cream Foundation 12G W50 CREME TAN\n\n"
                + "Make Over Powerstay Demi-Matte Cover Cushion W50 CREME TAN\n\n"
                + "Make Over Powerstay Total Cover Liquid Concealer 6.5 Ml MEDIUM\n\n"
                + "Make Over Powerstay 24H Matte Powder Foundation N50 TAN\n\n"
                + "Make Over Perfect Cover Two Way Cake 07 ESPRESSO",
            
                "Tone 7:\n"
                + "Powerstay 24H Weightless Liquid Foundation W60 CREME COCOA\n\n"
                + "Make Over Powerstay Total Cover Matte Cream Foundation 12G N50 TAN\n\n"
                + "Make Over Powerstay Demi-Matte Cover Cushion W60 CREME COCOA\n\n"
                + "Make Over Powerstay Total Cover Liquid Concealer 6.5 Ml MEDIUM\n\n"
                + "Make Over Powerstay 24H Matte Powder Foundation W60 CREME COCOA\n\n"
                + "Make Over Perfect Cover Two Way Cake 06 CAPPUCINO",
            
                "Tone 8: TAN TO DEEP WITH WARM RED UNDERTONE\n"
                + "Powerstay 24H Weightless Liquid Foundation C62 RICH COCOA\n\n"
                + "Make Over Powerstay Total Cover Matte Cream Foundation 12G C62 RICH COCOA\n\n"
                + "Make Over Powerstay Demi-Matte Cover Cushion C62 RICH COCOA\n\n"
                + "Make Over Powerstay Total Cover Liquid Concealer 6.5 Ml MEDIUM"            
        };        

        for (int i = 0; i < 7; i++) {
            centerPanel.add(createSetRow(i % 2 == 0, i + 1, descriptions[i], bodyFont));
            centerPanel.add(Box.createRigidArea(new Dimension(0, 40)));
        }

        JScrollPane scrollPane = new JScrollPane(centerPanel);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
        scrollPane.getVerticalScrollBar().setUnitIncrement(20);
        scrollPane.getViewport().setBackground(new Color(255, 240, 245));
        add(scrollPane, BorderLayout.CENTER);
    }

    private JPanel createSetRow(boolean imageLeft, int setNumber, String text, Font font) {
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.X_AXIS));
        panel.setOpaque(false);

        JPanel imageGrid = new JPanel(new GridLayout(2, 2, 10, 10));
        imageGrid.setPreferredSize(new Dimension(600, 600));
        imageGrid.setOpaque(false);

        for (int i = 1; i <= 4; i++) {
            JLabel imgLabel;
            String imgPath = "D:\\Code\\FINALBANGWT\\imagess\\set" + setNumber + "_" + i + ".png";
            ImageIcon icon = new ImageIcon(imgPath);
            if (icon.getIconWidth() > 0) {
                Image scaled = icon.getImage().getScaledInstance(280, 280, Image.SCALE_SMOOTH);
                imgLabel = new JLabel(new ImageIcon(scaled));
            } else {
                imgLabel = new JLabel("Image Not Found", SwingConstants.CENTER);
                imgLabel.setFont(font.deriveFont(Font.ITALIC, 14f));
            }
            imgLabel.setPreferredSize(new Dimension(280, 280));
            imgLabel.setBorder(new LineBorder(Color.GRAY, 1));
            imgLabel.setOpaque(true);
            imgLabel.setBackground(Color.WHITE);
            imageGrid.add(imgLabel);
        }

        JTextArea textArea = new JTextArea(text);
        textArea.setWrapStyleWord(true);
        textArea.setLineWrap(true);
        textArea.setEditable(false);
        textArea.setFocusable(false);
        textArea.setFont(font);
        textArea.setBackground(new Color(255, 225, 235));
        textArea.setBorder(new EmptyBorder(20, 20, 20, 20));

        JPanel textPanel = new JPanel(new BorderLayout());
        textPanel.setPreferredSize(new Dimension(600, 600));
        textPanel.setBackground(Color.WHITE);
        textPanel.setBorder(new LineBorder(new Color(180, 180, 180), 1));
        textPanel.add(textArea, BorderLayout.CENTER);

        if (imageLeft) {
            panel.add(imageGrid);
            panel.add(Box.createRigidArea(new Dimension(20, 0)));
            panel.add(textPanel);
        } else {
            panel.add(textPanel);
            panel.add(Box.createRigidArea(new Dimension(20, 0)));
            panel.add(imageGrid);
        }

        return panel;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new FashionRecs().setVisible(true);
        });
    }
}
