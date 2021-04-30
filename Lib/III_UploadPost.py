import os
import urllib.request


## 3. Delete REMOVE_ME & Upload the chosen post
from Lib.I_CleanStart import clean_start


def upload_post(sample, _bot, photo_link, post_caption, page_username):
    global orange_insta_hash
    if sample:
        # insta_hash = "000000000"
        orange_insta_hash = "CNxT8tPDe71" # Orange testing bot
        # photo_link = f"https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/175486994_989882978491793_6819629786327322759_n.jpg?tp=1&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=RteDikDW0UAAX_10Bvo&edm=AABBvjUBAAAA&ccb=7-4&oh=a146adced1dab5995018aa61286b349d&oe=60B0BC91&_nc_sid=83d603"
        # photo_link= "https://www.instagram.com/p/CNxT8tPDe71/" # Orange testing bot
    else: # On real upload.
        try:
            print('Delete "LastedPhoto.jpg.REMOVE_ME"')
            os.remove('LastedPhoto.jpg.REMOVE_ME')
        except:
            print('Error Delete "LastedPhoto.jpg.REMOVE_ME"')

        urllib.request.urlretrieve(f"{photo_link}", "LastedPhoto.jpg")

    try:
        response = _bot.upload_photo("LastedPhoto.jpg",
                                     caption=f"""{post_caption}
                                 post credit:@{page_username}""")

        # print("response: ")
        # print(response)
        insta_hash = response["code"]
    except Exception as e:
        # print("AAA")
        e = str(e)
        insta_hash = f"{orange_insta_hash}\nNot Upload since: \n{e}\nC U NXT Time!"
        print(insta_hash)
    return insta_hash



## Example
# bot, L = clean_start(username="3deal.com_", password="3deal3252", sample=True)
# print(bot)
# print(type(bot))

upload_post(sample=True, _bot="Doesnt matter", photo_link="Doesnt matter",
            post_caption="post_caption", page_username="3deal.com_")

## Response example:
# {
#   'taken_at': 1618677434,
#   'pk': 2553973886771659455,
#   'id': '2553973886771659455_44739760882',
#   'device_timestamp': 1618677416727,
#   'media_type': 1,
#   'code': 'CNxibfupgK_',
#   'client_cache_key': 'MjU1Mzk3Mzg4Njc3MTY1OTQ1NQ==.2',
#   'filter_type': 0,
#   'user': {
#     'pk': 44739760882,
#     'username': 'spider3d_models',
#     'full_name': '�Spider3D•Printspecialist',
#     'is_private': False,
#     'profile_pic_url': 'https: //instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/173212887_166065512048571_4193158418520845970_n.jpg?tp=1&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_ohc=bK8fBMLubmAAX_OjCWK&edm=ACqnv0EAAAAA&ccb=7-4&oh=bdd200fa832115a07603b0ff4f3156ad&oe=60A147A2&_nc_sid=9ec724',
#     'profile_pic_id': '2551800845358795229_44739760882',
#     'has_anonymous_profile_picture': False,
#     'can_boost_post': True,
#     'can_see_organic_insights': True,
#     'show_insights_terms': False,
#     'reel_auto_archive': 'unset',
#     'is_unpublished': False,
#     'allowed_commenter_type': 'any',
#     'account_badges': [
#
#     ],
#     'fbid_v2': 17841444666472470
#   },
#   'can_viewer_reshare': True,
#   'caption_is_edited': False,
#   'like_and_view_counts_disabled': False,
#   'is_paid_partnership': False,
#   'comment_likes_enabled': False,
#   'comment_threading_enabled': False,
#   'has_more_comments': False,
#   'max_num_visible_preview_comments': 2,
#   'preview_comments': [
#
#   ],
#   'can_view_more_preview_comments': False,
#   'comment_count': 0,
#   'hide_view_all_comment_entrypoint': False,
#   'image_versions2': {
#     'candidates': [
#       {
#         'width': 720,
#         'height': 592,
#         'url': 'https: //instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/e35/174584671_803365816944381_2493592352064454175_n.jpg?tp=1&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=uKVL6nwAYsQAX9JReQO&edm=ACqnv0EAAAAA&ccb=7-4&oh=6285d5a03d65192b4d3cfa1b11ca882c&oe=60A21DF5&_nc_sid=9ec724&ig_cache_key=MjU1Mzk3Mzg4Njc3MTY1OTQ1NQ%3D%3D.2-ccb7-4',
#         'scans_profile': 'e35',
#         'estimated_scans_sizes': [
#           6408,
#           12817,
#           19226,
#           25635,
#           32043,
#           38677,
#           46822,
#           52144,
#           57679
#         ]
#       },
#       {
#         'width': 360,
#         'height': 296,
#         'url': 'https: //instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/e35/s360x360/174584671_803365816944381_2493592352064454175_n.jpg?tp=1&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=uKVL6nwAYsQAX9JReQO&edm=ACqnv0EAAAAA&ccb=7-4&oh=698b1301a65434ae6aaed5a1fd943c8e&oe=609F8AA7&_nc_sid=9ec724&ig_cache_key=MjU1Mzk3Mzg4Njc3MTY1OTQ1NQ%3D%3D.2-ccb7-4',
#         'scans_profile': 'e35',
#         'estimated_scans_sizes': [
#           2460,
#           4921,
#           7381,
#           9842,
#           12302,
#           15358,
#           198350,
#           22145,
#           22145
#         ]
#       }
#     ]
#   },
#   'original_width': 720,
#   'original_height': 592,
#   'boosted_status': 'not_boosted',
#   'photo_of_you': False,
#   'can_see_insights_as_brand': False,
#   'caption': {
#     'pk': 17864412209436375,
#     'user_id': 44739760882,
#     'text': 'firstprintwith@epax3dE10�\nFantasticmodelby@wwtavern\n————————————————\nResin: @esun3dprinting\nPrinter: @epax3d\nSlicer: @chitubox_official\nModel: @wwtavern\n———————————————\n#3dprinter#3dprinting#3dmodel#3d#3dmodel#3dmodelling#3dprinted#3dmaker#maker#technology#gadget#impression3d#3dprints#pictureoftheday#toptags#stampa3d#instagood#awesome#tech#instapic#instalike#cool#makersmovement#makersgonnamake#resinprinter#resin#resinprinting#resina#3dresin\npostcredit: @crazyfilament',
#     'type': 1,
#     'created_at': 1618677435,
#     'created_at_utc': 1618677435,
#     'content_type': 'comment',
#     'status': 'Active',
#     'bit_flags': 0,
#     'did_report_as_spam': False,
#     'share_enabled': False,
#     'user': {
#       'pk': 44739760882,
#       'username': 'spider3d_models',
#       'full_name': '�Spider3D•Printspecialist',
#       'is_private': False,
#       'profile_pic_url': 'https: //instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/173212887_166065512048571_4193158418520845970_n.jpg?tp=1&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_ohc=bK8fBMLubmAAX_OjCWK&edm=ACqnv0EAAAAA&ccb=7-4&oh=bdd200fa832115a07603b0ff4f3156ad&oe=60A147A2&_nc_sid=9ec724',
#       'profile_pic_id': '2551800845358795229_44739760882',
#       'has_anonymous_profile_picture': False,
#       'can_boost_post': True,
#       'can_see_organic_insights': True,
#       'show_insights_terms': False,
#       'reel_auto_archive': 'unset',
#       'is_unpublished': False,
#       'allowed_commenter_type': 'any',
#       'account_badges': [
#
#       ],
#       'fbid_v2': 17841444666472470
#     },
#     'is_covered': False,
#     'media_id': 2553973886771659455,
#     'private_reply_status': 0
#   },
#   'fb_user_tags': {
#     'in': [
#
#     ]
#   },
#   'can_viewer_save': True,
#   'organic_tracking_token': 'eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODc1ZjBmODlmZmI5NGJjNmI1Mzc3NjkzMmFkYjViZjkyNTUzOTczODg2NzcxNjU5NDU1Iiwic2VydmVyX3Rva2VuIjoiMTYxODY3NzQzOTMwNHwyNTUzOTczODg2NzcxNjU5NDU1fDQ0NzM5NzYwODgyfDhlZGVmYzcyNjM3ODhhZTc3NDI2NjRmZmM0YTc2ZTY3YWIyMzk4ODU5N2MyODU3N2U2NDE0YzRjOWQ2ZjBmNDcifSwic2lnbmF0dXJlIjoiIn0=',
#   'sharing_friction_info': {
#     'should_have_sharing_friction': False,
#     'bloks_app_url': None
#   },
#   'product_type': 'feed',
#   'is_in_profile_grid': False,
#   'profile_grid_control_enabled': False,
#   'deleted_reason': 0,
#   'integrity_review_decision': 'pending'
# }