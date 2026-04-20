from django.shortcuts import render, get_object_or_404
from .models import Game, Genre

def game_list(request):
    games = Game.objects.all()
    genres = Genre.objects.all()
    context = {'games': games, 'genres': genres}
    return render(request, 'games/game_list.html', context)

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    channels = game.channel_set.all()
    context = {'game': game, 'channels': channels}
    return render(request, 'games/game_detail.html', context)