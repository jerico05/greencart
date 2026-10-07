from flask import Blueprint, jsonify, request, current_app
from dataclasses import asdict
from .yeria_views import (home_view,available_products_view, 
                          available_promotion_view,search_results_view,search_view, 
                          product_details_view,promotion_details_view,create_business_view,
                          store_management_view)

yeria_app = Blueprint("yeria_app", __name__)


def _yeria():
    return current_app.extensions["yeria"]


def serve(view, status=200):
    envelope = _yeria().serve(view)
    return jsonify(asdict(envelope)), status


def serve_error(code, message, status=400, invalid_params=None):
    envelope = _yeria().serve_error(code, message, status, invalid_params)
    return jsonify(asdict(envelope)), status


@yeria_app.route("/", methods=["GET"])
def home_screen():
    return serve(home_view())

@yeria_app.route("/available-products", methods=["GET"])
def available_products_screen():
    return serve(available_products_view())

@yeria_app.route("/available-promotions", methods=["GET"])
def available_pro_screen():
    return serve(available_promotion_view())

@yeria_app.route("/produit-1", methods=["GET"])
def product_details_screen():
    return serve(product_details_view())

@yeria_app.route("/promot-1", methods=["GET"])
def promotion_details_screen():
    return serve(promotion_details_view())

@yeria_app.route("/search", methods=["GET"])
def search_screen():
    return serve(search_view())

@yeria_app.route("/search-results", methods=["GET"])
def search_result_screen():
    return serve(search_results_view())

@yeria_app.route("/manage", methods=["GET"])
def store_management_screen():
    return serve(create_business_view())
    