import utils
import requests
import block_services


if __name__ == '__main__':
    utils.init_results_dir()
    
    requests_session = requests.Session()
    # url = "https://vnexpress.net/bo-truong-tai-chinh-gan-du-tien-tiem-vaccine-cho-75-trieu-dan-4299554.html"
    # url = "http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/"
    # url = "https://tuoitre.vn/chieu-25-6-ca-nuoc-them-102-ca-covid-19-tp-hcm-co-nhieu-ca-mac-cho-bo-y-te-cong-bo-20210625181028187.htm"
    # url = "https://vietnamnet.vn/vn/suc-khoe/ca-covid-19-phia-nam-phat-benh-chi-sau-hon-30-gio-tiep-xuc-750859.html"
    # url = "https://vtc.vn/phat-30-thang-tu-cuu-trung-uy-cong-an-thu-sung-lam-chet-nam-sinh-vien-ar621012.html"
    # url = "https://dantri.com.vn/the-thao/doi-tuyen-phap-bi-loai-soc-o-euro-2020-noi-dau-cua-su-ngao-man-20210629140900794.htm#dt_source=Home&dt_campaign=Cover&dt_medium=1"
    # url = "https://nld.com.vn/suc-khoe/khoa-cap-cuu-benh-vien-ba-ria-vua-bi-phong-toa-20210629141008312.htm"
    url = "https://thanhnien.vn/thoi-su/1-trieu-lieu-vac-xin-nhat-ban-tang-se-den-viet-nam-vao-17-va-87-1406260.html"
    response = utils.clone_page(requests_session, url)

    str_html = block_services.preprocess(response.text)
    blocks = block_services.divide_blocks(str_html)
    main_content = block_services.get_main_content(blocks)

    utils.dump_file(main_content, "main_content.txt")