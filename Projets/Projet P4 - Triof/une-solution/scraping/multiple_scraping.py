from google_image_scraper import scrap_imgs

nb_imgs = 20

# Dirty subfolder
scrap_imgs('dirty', 'dirty plastic bottle', nb_imgs)
scrap_imgs('dirty', 'dirty plastic cutlery', nb_imgs)
scrap_imgs('dirty', 'dirty plastic cup', nb_imgs)

# Clean subfolder
scrap_imgs('clean', 'plastic bottle', nb_imgs)
scrap_imgs('clean', 'plastic cutlery', nb_imgs)
scrap_imgs('clean', 'plastic cup', nb_imgs)

